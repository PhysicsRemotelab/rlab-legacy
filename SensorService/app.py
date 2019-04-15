from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json, time, math

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)

@socketio.on('start_measurement')
def start_measurement(init):
    print('Starting measurement with conditions: ' + str(init))
    parsed = json.loads(init)
    count = int(parsed['count'])

    for i in range(count):
        emit('sensor', {"id":i+1, "dist":round(math.sin(i), 3)}, json=True)
        socketio.sleep(1)

    emit('finished')

if __name__ == '__main__':
    print('Started.')
    socketio.run(app, host='0.0.0.0', port=4500)
