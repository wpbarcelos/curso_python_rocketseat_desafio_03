from flask import Flask, render_template

from flask_socketio import SocketIO, emit


app = Flask(__name__)

socketio = SocketIO(app)

history = []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', history=history)


@socketio.on('connect')
def handle_connect():
    print("user connected")


@socketio.on("disconnect")
def handle_disconnect():
    print('user connect')


@socketio.on('message')
def handle_message(message):
    history.append(message)
    emit('message', message,  broadcast=True)


@socketio.on('writting')
def handle_writting(user):
    emit('writting', user, broadcast=True, include_self=False)


@socketio.on('stop_writting')
def handle_writting(user):
    emit('stop_writting', user, broadcast=True, include_self=False)


if __name__ == '__main__':
    socketio.run(app, debug=True)
