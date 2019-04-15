import serial
import numpy as np
import json, time, math
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)

@socketio.on('start_spectrometer')
def start_spectrometer(init):
    print('Starting spectrometer with conditions: ' + str(init))
    ser = serial.Serial(port='COM3', baudrate=115200, timeout=5)
    x = np.arange(0, 287)

    while True:
        try:
            reading = ser.readline().decode('ascii')
            data = reading.split(',')
            #data = np.array(data)[0:287]
            print(data)
            emit('spectrometer', {"data": data}, json=True)
        except:
            print('Error')

        socketio.sleep(3)

if __name__ == '__main__':
    print('Started.')
    socketio.run(app, host='0.0.0.0', port=4600)
