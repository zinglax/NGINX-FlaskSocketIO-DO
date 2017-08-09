from app import app
from app import socketio
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send
from flask_socketio import emit



io_library = """
<script type='text/javascript' src='//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js'></script>
<script
  src="http://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script>
  
<script type='text/javascript' charset='utf-8'>
    var socket = io.connect('http://' + '192.168.1.27' + ':' + '5000');
        
    socket.on('connect', function() {
        socket.emit('my event', {data: 'Im connected!'});
    });
    
    socket.on('yerp_back', function(msg) {
        console.log(msg)
    });
    

    
    $( document ).ready(function() {
        $('#yerper').click(function(){
            socket.emit('yerp', 'yeah I yerped at u.');
        })
    });
    
    
</script>
"""

page = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
{}
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

<input id="yerper" type="button" value="Emit Yerp!">


</body>
</html>

"""



@app.route('/')
def hello():
    return page.format(io_library)   


@socketio.on('my event')
def handle_message(message):
    print('received message: ' + str(message))

    
@socketio.on('yerp')
def handle_message(message):
    print('received message: ' + str(message))
    emit('yerp_back', {'data': 'yahooooooooozers'})