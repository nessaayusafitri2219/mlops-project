"""
Script untuk testing API dan menghasilkan screenshot data
"""
import requests
import json
import time

def test_api():
    base_url = "http://localhost:8000"
    
    print("=" * 60)
    print("🧪 TESTING MLOPS API")
    print("=" * 60)
    
    # Test 1: Health Check
    print("\n1. Testing Health Endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Metrics
    print("\n2. Testing Metrics Endpoint...")
    try:
        response = requests.get(f"{base_url}/metrics")
        print(f"   Status Code: {response.status_code}")
        print(f"   Sample Metrics:")
        lines = response.text.split('\n')[:10]
        for line in lines:
            if line and not line.startswith('#'):
                print(f"   {line}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Prediction
    print("\n3. Testing Prediction Endpoint...")
    test_data = {
        "features": [5.1, 3.5, 1.4, 0.2]
    }
    try:
        response = requests.post(
            f"{base_url}/predict",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"   Status Code: {response.status_code}")
        print(f"   Request: {json.dumps(test_data, indent=2)}")
        print(f"   Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Multiple Predictions
    print("\n4. Testing Multiple Predictions...")
    test_cases = [
        [5.1, 3.5, 1.4, 0.2],
        [6.2, 2.9, 4.3, 1.3],
        [7.3, 2.9, 6.3, 1.8]
    ]
    
    for i, features in enumerate(test_cases, 1):
        try:
            response = requests.post(
                f"{base_url}/predict",
                json={"features": features}
            )
            result = response.json()
            print(f"   Test {i}: {features} -> {result}")
        except Exception as e:
            print(f"   ❌ Test {i} Error: {e}")
    
    print("\n" + "=" * 60)
    print("✅ TESTING COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    print("\n⚠️  Pastikan API sudah berjalan di http://localhost:8000")
    print("    Jalankan: python app.py\n")
    
    input("Press Enter untuk mulai testing...")
    test_api()
