#!/usr/bin/env python3
import sys
import os
import json

# Symulacja CGI environment
os.environ['REQUEST_METHOD'] = 'POST'
test_data = '{"qr_code": "QR-EMP-001", "user_id": "1"}'
os.environ['CONTENT_LENGTH'] = str(len(test_data))

# Symulacja stdin
import io
sys.stdin = io.StringIO(test_data)

# Importuj i uruchom CGI
exec(open('/app/qr_scan.cgi').read())