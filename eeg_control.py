# Importing the packages and the libraries
from credentials import *
import json
from websocket import create_connection
import ssl
import time
import requests

# Create object of class create_connection
ws = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})

# Create a session with the Emotiv Insight
ws.send(json.dumps({
 "jsonrpc": "2.0",
 "method": "createSession",
 "params": {
     "_auth": _auth,
     "headset":"INSIGHT-5A688F16",
     "status": "open"
 },
 "id": 1
 }))

print(ws.recv())

# Subscribe to sys stream
ws.send(json.dumps({
 "jsonrpc": "2.0",
 "method": "subscribe", 
 "params": {
     "_auth":_auth,
     "streams":[
     "sys"
     ]
 },
 "id": 1
 }))

print(ws.recv())

# Begin training mental commands

# Training neutral
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "_auth":_auth,
   "detection":"mentalCommand",
   "action":"neutral",
   "status":"start"
 }, 
 "id": 1
 }))

print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "_auth":_auth,
     "detection":"mentalCommand",
     "action":"neutral",
     "status":"accept"
 }, 
 "id": 1
 }
))

print(ws.recv())
time.sleep(2)
print(ws.recv())


# Training push (forward)
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "_auth":_auth,
   "detection":"mentalCommand",
   "action":"push",
   "status":"start"
 }, 
 "id": 1
 }))

print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "_auth":_auth,
     "detection":"mentalCommand",
     "action":"push",
     "status":"accept"
 }, 
 "id": 1
 }
))

print(ws.recv())
time.sleep(2)
print(ws.recv())

# Training left (pivot left)
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "_auth":_auth,
   "detection":"mentalCommand",
   "action":"left",
   "status":"start"
 }, 
 "id": 1
 }))

print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "_auth":_auth,
     "detection":"mentalCommand",
     "action":"left",
     "status":"accept"
 }, 
 "id": 1
 }
))

print(ws.recv())
time.sleep(2)
print(ws.recv())

# Training right (pivot right)
ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
   "_auth":_auth,
   "detection":"mentalCommand",
   "action":"right",
   "status":"start"
 }, 
 "id": 1
 }))

print(ws.recv())
time.sleep(5)
print(ws.recv())
time.sleep(10)
print(ws.recv())

ws.send(json.dumps( {
 "jsonrpc": "2.0", 
 "method": "training", 
 "params": {
     "_auth":_auth,
     "detection":"mentalCommand",
     "action":"right",
     "status":"accept"
 }, 
 "id": 1
 }
))

print(ws.recv())
time.sleep(2)
print(ws.recv())

# Obtain stream of mental commands

# Subscribe to com stream
ws.send(json.dumps({
 "jsonrpc": "2.0",
 "method": "subscribe", 
 "params": {
     "_auth":_auth,
     "streams":[
     "com"
 ]
 },
 "id": 1
 }))

print(ws.recv())

# loop for rover control
while True:
 thought = json.loads(ws.recv())["com"][0]
 print(thought)
 
 if(thought == "push"):
     url_get = "http://192.168.0.8:5000/forward"
     res = requests.get(url_get)
 elif(thought == "left"):
     url_get = "http://192.168.0.8:5000/pivot_left"
     res = requests.get(url_get)
 elif(thought == "right"):
     url_get = "http://192.168.0.8:5000/pivot_right"
     res = requests.get(url_get)
