#!/usr/bin/python3

import subprocess
import cgi

print('content-type: text/html')
# allowing CORS because frontend is hosted on different server
print('Access-Control-Allow-Origin: *') # anyone can access or some defined IP addresses
print()

# get the values from the URL
vars = cgi.FieldStorage()
cmd = vars.getvalue('cmd')

# saving and returning the output
output = subprocess.getoutput("sudo "+cmd)

print(output)
