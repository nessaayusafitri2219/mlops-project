from flask import Flask, request, jsonify
import joblib
import numpy as np
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
import os

app = Flask(__name__)

# Load model
MODEL_PATH = "models/model.pkl"
model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully!")
else:
    print(f"Warning: Model not found at {MODEL_PATH}")

# Prometheus metrics
REQUEST_COUNT = Counter('api_requests_total', 'Total API requests', ['method', 'endpoint', 'status'])
REQUEST_DURATION = Histogram('api_request_duration_seconds', 'API request duration')
PREDICTION_COUNT = Counter('predictions_total', 'Total predictions made')
MODEL_ACCURACY = Gauge('model_accuracy', 'Current model accuracy')

# Set initial accuracy from metrics.json if available
if os.path.exists("models/metrics.json"):
    import json
    with open("models/metrics.json", "r") as f:
        metrics = json.load(f)
        MODEL_ACCURACY.set(metrics.get("accuracy", 0))

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    start_time = time.time()
    
    status = "healthy" if model is not None else "unhealthy"
    response = jsonify({"status": status})
    
    duration = time.time() - start_time
    REQUEST_DURATION.observe(duration)
    REQUEST_COUNT.labels(method='GET', endpoint='/health', status=200).inc()
    
    return response, 200

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint"""
    start_time = time.time()
    
    try:
        if model is None:
            REQUEST_COUNT.labels(method='POST', endpoint='/predict', status=500).inc()
            return jsonify({"error": "Model not loaded"}), 500
        
        data = request.get_json()
        
        if not data or 'features' not in data:
            REQUEST_COUNT.labels(method='POST', endpoint='/predict', status=400).inc()
            return jsonify({"error": "Missing 'features' in request"}), 400
        
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)
        
        PREDICTION_COUNT.inc()
        
        duration = time.time() - start_time
        REQUEST_DURATION.observe(duration)
        REQUEST_COUNT.labels(method='POST', endpoint='/predict', status=200).inc()
        
        return jsonify({
            "prediction": int(prediction[0]),
            "probability": prediction_proba[0].tolist(),
            "duration_seconds": duration
        }), 200
        
    except Exception as e:
        REQUEST_COUNT.labels(method='POST', endpoint='/predict', status=500).inc()
        return jsonify({"error": str(e)}), 500

@app.route('/metrics', methods=['GET'])
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    REQUEST_COUNT.labels(method='GET', endpoint='/', status=200).inc()
    return jsonify({
        "service": "MLOps Model API",
        "version": "1.0.0",
        "endpoints": {
            "/health": "Health check",
            "/predict": "Make predictions (POST)",
            "/metrics": "Prometheus metrics"
        }
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
