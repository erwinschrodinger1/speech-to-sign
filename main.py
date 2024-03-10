import os
from flask import Flask, render_template
from flask_socketio import SocketIO
from dotenv import load_dotenv


app = Flask(__name__, static_folder='templates', static_url_path="")
socketio = SocketIO(app)

load_dotenv()


@app.route('/')
def hello():
    apiKey = os.getenv('SPEECH_KEY')
    region = os.getenv('SPEECH_REGION')
    return render_template('index.html', apiKey=apiKey, region=region)


@socketio.on('audio')
def handle_message(data):
    print(data)


if __name__ == "__main__":
    print("Running the app")
    socketio.run(app, debug=True)
