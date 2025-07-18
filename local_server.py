#!/usr/bin/env python3
"""
Local HTTP Server for TimeTracker Pro
Runs the application locally without CGI hosting
"""
import http.server
import socketserver
import json
import os
import sys
from urllib.parse import urlparse, parse_qs
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import Database
from auth import verify_password, create_access_token, parse_datetime, init_default_data

class TimeTrackerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()

    def add_cors_headers(self):
        """Add CORS headers to response"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Access-Control-Allow-Credentials', 'true')

    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # API endpoints
        if path.startswith('/api/'):
            self.handle_api_request('GET', path, None)
        # Serve index.html for root path
        elif path == '/':
            self.serve_index()
        # Serve static files
        elif path.startswith('/static/'):
            super().do_GET()
        # Serve specific HTML files
        elif path.endswith('.html'):
            self.serve_html_file(path[1:])  # Remove leading slash
        else:
            # For any other path, serve index.html (SPA routing)
            self.serve_index()

    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = None
        if content_length > 0:
            body_bytes = self.rfile.read(content_length)
            try:
                body = json.loads(body_bytes.decode('utf-8'))
            except json.JSONDecodeError:
                self.send_error_response("Invalid JSON", 400)
                return
        
        if path.startswith('/api/'):
            self.handle_api_request('POST', path, body)
        else:
            self.send_error_response("Not Found", 404)

    def serve_index(self):
        """Serve the main index.html file"""
        try:
            with open('index.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.add_cors_headers()
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.send_error_response("Index file not found", 404)

    def serve_html_file(self, filename):
        """Serve a specific HTML file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.add_cors_headers()
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.send_error_response(f"File {filename} not found", 404)

    def handle_api_request(self, method, path, body):
        """Handle API requests"""
        try:
            # Initialize database
            db = Database()
            db.init_db()
            init_default_data()
            
            # Route API calls
            if path == '/api/login' and method == 'POST':
                self.handle_login(body, db)
            elif path == '/api/init' and method == 'GET':
                self.handle_init(db)
            elif path == '/api/test' and method == 'GET':
                self.handle_test()
            elif path == '/api/users' and method == 'GET':
                self.handle_get_users(db)
            elif path == '/api/companies' and method == 'GET':
                self.handle_get_companies(db)
            elif path == '/api/employees' and method == 'GET':
                self.handle_get_employees(db)
            else:
                self.send_error_response("API endpoint not found", 404)
                
        except Exception as e:
            self.send_error_response(f"Server error: {str(e)}", 500)

    def handle_login(self, body, db):
        """Handle login request"""
        if not body:
            self.send_error_response("Request body required", 400)
            return
        
        username = body.get('username')
        password = body.get('password')
        
        if not username or not password:
            self.send_error_response("Username and password required", 400)
            return
        
        # Find user
        user = db.find_one("users", {"username": username})
        if not user or not verify_password(password, user["password_hash"]):
            self.send_error_response("Invalid credentials", 401)
            return
        
        # Create access token
        access_token = create_access_token({"user_id": user["id"]})
        
        # Get company name
        company_name = user.get("company_name")
        if user.get("company_id"):
            company = db.find_one("companies", {"id": user["company_id"]})
            if company:
                company_name = company["name"]
        
        # Parse datetime
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
        
        self.send_json_response(response)

    def handle_init(self, db):
        """Handle initialization request"""
        try:
            db.init_db()
            init_default_data()
            
            response = {
                "message": "Database initialized successfully",
                "status": "ready",
                "default_accounts": {
                    "owner": "owner/owner123",
                    "admin": "admin/admin123",
                    "user": "user/user123"
                }
            }
            self.send_json_response(response)
        except Exception as e:
            self.send_error_response(f"Database initialization failed: {str(e)}", 500)

    def handle_test(self):
        """Handle test request"""
        response = {
            "message": "TimeTracker Pro Local Server is running!",
            "status": "ok",
            "version": "1.0.0"
        }
        self.send_json_response(response)

    def handle_get_users(self, db):
        """Handle get users request"""
        users = db.find_many("users")
        # Remove password hashes from response
        for user in users:
            user.pop("password_hash", None)
        self.send_json_response(users)

    def handle_get_companies(self, db):
        """Handle get companies request"""
        companies = db.find_many("companies")
        self.send_json_response(companies)

    def handle_get_employees(self, db):
        """Handle get employees request"""
        employees = db.find_many("employees")
        self.send_json_response(employees)

    def send_json_response(self, data, status_code=200):
        """Send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.add_cors_headers()
        self.end_headers()
        
        json_data = json.dumps(data, default=str, ensure_ascii=False)
        self.wfile.write(json_data.encode('utf-8'))

    def send_error_response(self, message, status_code=400):
        """Send error response"""
        error_data = {"error": message}
        self.send_json_response(error_data, status_code)

    def log_message(self, format, *args):
        """Override log message to show API calls"""
        print(f"[{self.address_string()}] {format % args}")

def main():
    PORT = 8080
    
    # Ensure database is initialized
    print("Initializing TimeTracker Pro...")
    try:
        db = Database()
        db.init_db()
        init_default_data()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return
    
    # Start server
    with socketserver.TCPServer(("", PORT), TimeTrackerHandler) as httpd:
        print(f"🚀 TimeTracker Pro Local Server started on http://localhost:{PORT}")
        print(f"📱 Open your browser and go to: http://localhost:{PORT}")
        print(f"🔑 Default accounts:")
        print(f"   - owner/owner123 (System Owner)")
        print(f"   - admin/admin123 (Company Admin)")
        print(f"   - user/user123 (Employee)")
        print(f"💻 API available at: http://localhost:{PORT}/api/")
        print(f"🛑 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")

if __name__ == "__main__":
    main()