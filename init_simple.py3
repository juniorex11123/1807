#!/usr/bin/python3
"""
Database initialization endpoint for TimeTracker Pro
URL: https://TWOJA-DOMENA.home.pl/init.py3
Run this once to initialize the database
"""

# Dodaj CORS headers na początku
print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS")
print("Access-Control-Allow-Headers: Content-Type, Authorization")
print("Access-Control-Allow-Credentials: true")
print()

try:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    from database import Database
    from auth import init_default_data
    
    # Inicjalizuj bazę danych
    db = Database()
    db.init_db()
    init_default_data()
    
    import json
    result = {
        "message": "Database initialized successfully",
        "status": "ready",
        "default_accounts": {
            "owner": "owner/owner123",
            "admin": "admin/admin123", 
            "user": "user/user123"
        }
    }
    print(json.dumps(result))
    
except Exception as e:
    import json
    error_result = {
        "message": f"Database initialization failed: {str(e)}",
        "status": "error",
        "error_type": type(e).__name__
    }
    print(json.dumps(error_result))