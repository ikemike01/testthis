#!/usr/bin/env python3
"""
Simple test script to verify the FastAPI signup form functionality.
This script tests various scenarios to ensure the API works correctly.
"""

import requests
import json
import time
import subprocess
import sys
import os

def test_api():
    """Test the FastAPI signup form API."""
    base_url = "http://localhost:8000"
    
    print("Testing FastAPI Signup Form API...")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        assert response.status_code == 200
        print("   ✓ Health check passed")
    except Exception as e:
        print(f"   ✗ Health check failed: {e}")
        return False
    
    # Test 2: Root endpoint
    print("\n2. Testing root endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        assert response.status_code == 200
        print("   ✓ Root endpoint passed")
    except Exception as e:
        print(f"   ✗ Root endpoint failed: {e}")
        return False
    
    # Test 3: Valid signup
    print("\n3. Testing valid signup...")
    valid_data = {
        "username": "testuser123",
        "email": "test@example.com",
        "password": "ValidPass123"
    }
    try:
        response = requests.post(f"{base_url}/signup", json=valid_data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        assert response.status_code == 200
        print("   ✓ Valid signup passed")
    except Exception as e:
        print(f"   ✗ Valid signup failed: {e}")
        return False
    
    # Test 4: Invalid username (non-alphanumeric)
    print("\n4. Testing invalid username...")
    invalid_username_data = {
        "username": "test@user",
        "email": "test@example.com",
        "password": "ValidPass123"
    }
    try:
        response = requests.post(f"{base_url}/signup", json=invalid_username_data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        assert response.status_code == 422
        print("   ✓ Invalid username validation passed")
    except Exception as e:
        print(f"   ✗ Invalid username validation failed: {e}")
        return False
    
    # Test 5: Invalid email
    print("\n5. Testing invalid email...")
    invalid_email_data = {
        "username": "testuser",
        "email": "invalid-email",
        "password": "ValidPass123"
    }
    try:
        response = requests.post(f"{base_url}/signup", json=invalid_email_data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        assert response.status_code == 422
        print("   ✓ Invalid email validation passed")
    except Exception as e:
        print(f"   ✗ Invalid email validation failed: {e}")
        return False
    
    # Test 6: Weak password
    print("\n6. Testing weak password...")
    weak_password_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "weak"
    }
    try:
        response = requests.post(f"{base_url}/signup", json=weak_password_data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        assert response.status_code == 422
        print("   ✓ Weak password validation passed")
    except Exception as e:
        print(f"   ✗ Weak password validation failed: {e}")
        return False
    
    # Test 7: Existing username
    print("\n7. Testing existing username...")
    existing_username_data = {
        "username": "admin",
        "email": "admin@example.com",
        "password": "ValidPass123"
    }
    try:
        response = requests.post(f"{base_url}/signup", json=existing_username_data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        assert response.status_code == 409
        print("   ✓ Existing username validation passed")
    except Exception as e:
        print(f"   ✗ Existing username validation failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("All tests passed! ✓")
    return True

if __name__ == "__main__":
    print("Please make sure the FastAPI server is running on localhost:8000")
    print("You can start it with: python app.py")
    print("Press Enter to continue with testing...")
    input()
    
    success = test_api()
    if success:
        print("\n🎉 All tests passed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)