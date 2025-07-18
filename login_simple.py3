#!/usr/bin/python3
"""
Login endpoint for TimeTracker Pro
URL: https://TWOJA-DOMENA.home.pl/login.py3
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Obsługa CORS preflight
request_method = os.environ.get('REQUEST_METHOD', 'GET')
if request_method == 'OPTIONS':
    print("Status: 200 OK")
    print("Content-Type: application/json")
    print("Access-Control-Allow-Origin: *")
    print("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS")
    print("Access-Control-Allow-Headers: Content-Type, Authorization")
    print("Access-Control-Allow-Credentials: true")
    print()
    sys.exit(0)

# Dodaj CORS headers
print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS")
print("Access-Control-Allow-Headers: Content-Type, Authorization")
print("Access-Control-Allow-Credentials: true")
print()

try:
    import json
    from database import Database
    from auth import verify_password, create_access_token, parse_datetime
    
    if request_method != 'POST':
        print(json.dumps({"error": "Method not allowed"}))
        sys.exit(1)
    
    # Odczytaj body
    content_length = int(os.environ.get('CONTENT_LENGTH', '0'))
    if content_length > 0:
        body_raw = sys.stdin.read(content_length)
        body = json.loads(body_raw)
    else:
        print(json.dumps({"error": "Request body required"}))
        sys.exit(1)
    
    username = body.get('username')
    password = body.get('password')
    
    if not username or not password:
        print(json.dumps({"error": "Username and password required"}))
        sys.exit(1)
    
    # Sprawdź użytkownika
    db = Database()
    user = db.find_one("users", {"username": username})
    
    if not user or not verify_password(password, user["password_hash"]):
        print(json.dumps({"error": "Invalid credentials"}))
        sys.exit(1)
    
    # Utwórz token
    access_token = create_access_token({"user_id": user["id"]})
    
    # Pobierz nazwę firmy
    company_name = user.get("company_name")
    if user.get("company_id"):
        company = db.find_one("companies", {"id": user["company_id"]})
        if company:
            company_name = company["name"]
    
    # Przygotuj odpowiedź
    created_at = parse_datetime(user["created_at"]) if isinstance(user["created_at"], str) else user["created_at"]
    
    user_response = {
        "id": user["id"],
        "username": user["username"],
        "type": user["type"],
        "role": user["role"],
        "company_id": user.get("company_id"),
        "company_name": company_name,
        "created_at": created_at.isoformat() if hasattr(created_at, 'isoformat') else created_at
    }
    
    response = {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user_response
    }
    
    print(json.dumps(response))
    
except Exception as e:
    import json
    error_response = {
        "error": f"Login failed: {str(e)}",
        "error_type": type(e).__name__
    }
    print(json.dumps(error_response))