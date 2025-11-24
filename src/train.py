"""
MLOps Training Script
Train machine learning model dengan MLflow tracking
"""
import os
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
from datetime import datetime

def load_data():
    """Load dataset"""
    print("📊 Loading dataset...")
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='target')
    return X, y

def preprocess_data(X, y, test_size=0.2, random_state=42):
    """Split data into train and test sets"""
    print("🔧 Preprocessing data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train, params=None):
    """Train Random Forest model"""
    print("🚀 Training model...")
    
    if params is None:
        params = {
            'n_estimators': 100,
            'max_depth': 10,
            'min_samples_split': 2,
            'min_samples_leaf': 1,
            'random_state': 42
        }
    
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    print("📈 Evaluating model...")
    
    y_pred = model.predict(X_test)
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1_score': f1_score(y_test, y_pred, average='weighted')
    }
    
    return metrics

def save_model(model, model_path='models'):
    """Save model to disk"""
    os.makedirs(model_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{model_path}/model_{timestamp}.pkl"
    
    joblib.dump(model, filename)
    print(f"💾 Model saved to: {filename}")
    
    # Also save as latest
    latest_path = f"{model_path}/model_latest.pkl"
    joblib.dump(model, latest_path)
    print(f"💾 Latest model saved to: {latest_path}")
    
    return filename

def main():
    """Main training pipeline"""
    print("="*60)
    print("🤖 MLOps Training Pipeline Started")
    print("="*60)
    
    # Set MLflow tracking URI
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("iris-classification")
    
    # Start MLflow run
    with mlflow.start_run():
        # Load data
        X, y = load_data()
        
        # Log dataset info
        mlflow.log_param("dataset", "iris")
        mlflow.log_param("n_samples", len(X))
        mlflow.log_param("n_features", X.shape[1])
        mlflow.log_param("n_classes", len(np.unique(y)))
        
        # Preprocess data
        X_train, X_test, y_train, y_test = preprocess_data(X, y)
        
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("train_samples", len(X_train))
        mlflow.log_param("test_samples", len(X_test))
        
        # Model parameters
        params = {
            'n_estimators': 100,
            'max_depth': 10,
            'min_samples_split': 2,
            'min_samples_leaf': 1,
            'random_state': 42
        }
        
        # Log parameters
        mlflow.log_params(params)
        
        # Train model
        model = train_model(X_train, y_train, params)
        
        # Evaluate model
        metrics = evaluate_model(model, X_test, y_test)
        
        # Log metrics
        mlflow.log_metrics(metrics)
        
        # Print results
        print("\n📊 Training Results:")
        print("-" * 40)
        for metric_name, metric_value in metrics.items():
            print(f"{metric_name.capitalize()}: {metric_value:.4f}")
        print("-" * 40)
        
        # Save model
        model_path = save_model(model)
        
        # Log model to MLflow
        mlflow.sklearn.log_model(model, "model")
        
        # Log model file as artifact
        mlflow.log_artifact(model_path)
        
        print("\n✅ Training completed successfully!")
        print("="*60)
        
        return metrics

if __name__ == "__main__":
    main()
