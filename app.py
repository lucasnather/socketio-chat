from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500/"}})
app.config["SECRET_KEY"] = "xiiesecretonateoria"

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html', host="http://127.0.0.1:5000")

@socketio.on('chat-message')
def handle_message(msg):
    emit('chat-message', msg, broadcast=True)

@socketio.on("connect")
def connect():
    print("Web socket connect")

@socketio.on("disconnect")
def disconnect():
    print("Web socket disconnect")

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)