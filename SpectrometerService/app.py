import asyncio
import websockets
import serial
import numpy as np
import json
from argparse import ArgumentParser

# 1. Convert pixels into wavelengths
x = (2.35 * np.linspace(0, 239, 240) + 319.16)

# 2. Open serial port
try:
    ser = serial.Serial('COM3', baudrate=115200, timeout=1)
except Exception as e:
    print(e)

# 3. Define websocket function
async def senddata(websocket, path):
    while True:
        # 4. Read data
        data = ser.readline()
        ser.flushInput()
        data2 = data.split(b',')

        # Instead of all 288, take 10-250.
        data3 = data2[10:250]

        # Check if 240 datapoints are returned
        if len(data3) ==  240:
            try:
                y_in = [int(p) for p in data3]
            except Exception as e:
                print(e)

            # 5. Convert data for javscript chart
            points = []
            for i in range(240):
                obj = {'x': float(x[i]), 'y': float(y_in[i])}
                points.append(obj)
            data = json.dumps({ 'data': points })

            # 6. Send data to client
            await websocket.send(data)
            # 7. Wait 1 second before sending next dataset
            await asyncio.sleep(1)
        
# Start server

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-host')
    parser.add_argument('-port')
    args = parser.parse_args()
    host = args.host
    port = int(args.port)

    start_server = websockets.serve(senddata, host, port)
    print('Started.')
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
