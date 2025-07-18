#!/usr/bin/env python3
"""
Test script for TimeTracker Pro API
"""
import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_api():
    print("🧪 Testing TimeTracker Pro API...")
    
    # Test server status
    try:
        response = requests.get(f"{BASE_URL}/test")
        print(f"✅ Server status: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"❌ Server connection failed: {e}")
        return
    
    # Test login
    login_data = {
        "username": "owner",
        "password": "owner123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        if response.status_code == 200:
            login_result = response.json()
            print(f"✅ Login successful: {login_result['user']['username']} ({login_result['user']['type']})")
            print(f"🔑 Token: {login_result['access_token'][:20]}...")
        else:
            print(f"❌ Login failed: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"❌ Login request failed: {e}")
    
    # Test other endpoints
    try:
        response = requests.get(f"{BASE_URL}/users")
        users = response.json()
        print(f"✅ Users endpoint: Found {len(users)} users")
        
        response = requests.get(f"{BASE_URL}/companies")
        companies = response.json()
        print(f"✅ Companies endpoint: Found {len(companies)} companies")
        
        response = requests.get(f"{BASE_URL}/employees")
        employees = response.json()
        print(f"✅ Employees endpoint: Found {len(employees)} employees")
        
    except Exception as e:
        print(f"❌ API test failed: {e}")

if __name__ == "__main__":
    test_api()