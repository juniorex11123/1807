#!/usr/bin/env python3
"""
Tester for CGI files before deployment to home.pl
"""
import os
import sys
import subprocess
import json

def test_cgi_file(filename):
    """Test if CGI file works"""
    print(f"🧪 Testing {filename}...")
    
    if not os.path.exists(filename):
        print(f"❌ File {filename} not found")
        return False
    
    # Set CGI environment
    env = os.environ.copy()
    env['REQUEST_METHOD'] = 'GET'
    env['SERVER_NAME'] = 'localhost'
    env['SERVER_PORT'] = '80'
    env['SCRIPT_NAME'] = '/' + filename
    
    try:
        result = subprocess.run(
            ['python3', filename],
            env=env,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✅ {filename} - SUCCESS")
            return True
        else:
            print(f"❌ {filename} - FAILED")
            print(f"   Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ {filename} - TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ {filename} - ERROR: {e}")
        return False

def main():
    print("🚀 Testing CGI files for home.pl deployment...")
    print("=" * 50)
    
    # List of CGI files to test
    cgi_files = [
        'test.py3',
        'init_simple.py3',
        'login_simple.py3',
        'init.py3',
        'login.py3',
        'users.py3',
        'companies.py3',
        'employees.py3'
    ]
    
    success_count = 0
    total_count = len(cgi_files)
    
    for filename in cgi_files:
        if test_cgi_file(filename):
            success_count += 1
    
    print("=" * 50)
    print(f"📊 Results: {success_count}/{total_count} files working")
    
    if success_count == total_count:
        print("✅ All CGI files are ready for deployment!")
        return True
    else:
        print("❌ Some CGI files have issues - check before deployment")
        return False

if __name__ == "__main__":
    main()