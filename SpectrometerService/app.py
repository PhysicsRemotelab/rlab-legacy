import asyncio
import datetime
import random
import websockets
import serial
from scipy import interpolate
import numpy as np
import json

# 1. Convert pixels into wavelengths
x = (2.35 * np.linspace(0, 239, 240) + 319.16)

# 6. Open serial port
try:
    ser = serial.Serial('COM3', baudrate=115200, timeout=1)
except Exception as e:
    print(e)

# 7. Define websocket function
async def senddata(websocket, path):
    while True:
        # 8. Read data
        data = ser.readline()
        ser.flushInput()
        data2 = data.split(b',')
        data3 = data2[10:250]
        if len(data3) ==  240:
            try:
                y_in = [int(p) for p in data3]
            except Exception as e:
                print(e)

            # 9. Convert data for javscript chart
            points = []
            for i in range(240):
                obj = {'x': float(x[i]), 'y': float(y_in[i])}
                points.append(obj)
            data = json.dumps({ 'data': points })

            # 10. Send data to client
            await websocket.send(data)
            # Wait 1 second
            await asyncio.sleep(1)
        
# Start server
start_server = websockets.serve(senddata, '0.0.0.0', 3003)
print('Started.')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
