from flask import Flask
from flask_socketio import SocketIO , emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app , cors_allowed_origins="*")


@socketio.on("connect")
def handle_connect():
    emit("serverData",{"type": "SEND_AGENT_CRED"} )


@socketio.on('event')
def handle_message(event_to_emit_back):
    print(event_to_emit_back)
    emit("serverData" , event_to_emit_back)
    



  

if __name__ == '__main__':
    socketio.run(app , host="localhost" , port=5001)
