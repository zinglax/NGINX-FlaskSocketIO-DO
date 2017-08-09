#!/usr/bin/python
from app import socketio
from app import app

# Configuration
HOST = '0.0.0.0'
PORT = 5000

# Run the app
socketio.run(app, host=HOST, port=PORT)
