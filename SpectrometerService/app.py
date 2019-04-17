import serial
import numpy as np
import json, time, math
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, logger=True, engineio_logger=True)

x = np.arange(0, 287).T

@socketio.on('start_spectrometer')
def start_spectrometer(init):
    print('Starting spectrometer with conditions: ' + str(init))
    parsed = json.loads(init)
    samples = int(parsed['samples'])
    interval = int(parsed['interval'])

    ser = serial.Serial(port='COM3', baudrate=115200, timeout=5)

    for i in range(samples):
        try:
            reading = ser.readline().decode('ascii')
            data = reading.split(',')
            y = np.array(data)[0:287] # Select all except last one, because it is new line \n
            #y = 100*np.random.rand(287).T

            points = []
            for i in range(287):
                obj = {'x': int(x[i]), 'y': int(y[i])}
                points.append(obj)

            emit('spectrometer', {"data": points}, json=True)
            print(np.mean(np.array(y).astype(np.float)))

        except Exception  as e:
            print(e)

        socketio.sleep(interval)

    emit('finished')

if __name__ == '__main__':
    print('Started.')
    socketio.run(app, host='0.0.0.0', port=4600)
