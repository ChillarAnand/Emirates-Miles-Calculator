#!/usr/bin/env python

import sys
import json
import cgi

class MyHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")        

    def do_GET(self):           
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type',    'text/html')                                    
        self.end_headers()              
        self.wfile.write("<html><body>Hello world!</body></html>")
        self.connection.shutdown(1) 



fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
