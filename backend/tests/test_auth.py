"""
Test Auth API
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_verify_pin_success():
    response = client.post("/api/verify-pin", json={"pin": "123456"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert data["message"] == "Xác thực thành công"

def test_verify_pin_fail():
    response = client.post("/api/verify-pin", json={"pin": "000000"})
    assert response.status_code == 401

def test_verify_pin_invalid_format():
    response = client.post("/api/verify-pin", json={"pin": "abc"})
    assert response.status_code == 401

if __name__ == "__main__":
    print("[TEST] test_verify_pin_success...")
    test_verify_pin_success()
    print("[OK]")
    
    print("[TEST] test_verify_pin_fail...")
    test_verify_pin_fail()
    print("[OK]")
    
    print("[TEST] test_verify_pin_invalid_format...")
    test_verify_pin_invalid_format()
    print("[OK]")
    
    print("\n[INFO] Tất cả tests đã pass!")
