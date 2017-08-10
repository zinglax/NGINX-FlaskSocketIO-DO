#!/usr/bin/python
from app import socketio
from app import app

# Configuration
HOST = '127.0.0.1'
PORT = 5000

# Run the app
socketio.run(app, host=HOST, port=PORT)
