import asyncio
import datetime
import random
import websockets
import serial
from scipy import interpolate
import numpy as np
import json

# 1. Convert pixels into wavelengths
x = (2.35 * np.linspace(10, 250, 240) + 319.16) * 10e-10

# 2. Create model to describe uncalibrated line
wavelength = np.round(np.genfromtxt('SpectrometerCalibration/xval.txt', delimiter='\n'))
wavelength = wavelength * 10e-10
intensity = np.genfromtxt('SpectrometerCalibration/yval.txt', delimiter=',')
uncalibrated_line = interpolate.interp1d(wavelength, intensity, kind='cubic')

# 3. Create model to describe black body line 
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
T = 1700 + 273
blackbody_line = 2.0*h*c**2 / ((x**5) * (np.exp(h*c/(x*k*T)) - 1.0)) * 10e-9

# 4. Calculate coefficients and function
uncalibrated_y = uncalibrated_line(x)
coef = blackbody_line / uncalibrated_y
coef_func = interpolate.interp1d(x, coef, kind='cubic')

# 5. Calculate wavelengths and real intensities
wavelengths = (2.35 * np.linspace(10, 250, 240) + 319.16) * 10e-10
percent = coef_func(wavelengths)
y_in = np.zeros((0, 240))
wavelengths = wavelengths * 10e+8

# 6. Open serial port
try:
    ser = serial.Serial('COM5', baudrate=115200, timeout=1)
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
            y_in = [int(p) for p in data3]
            real_intensities = percent * y_in
            real_intensities = real_intensities / max(real_intensities) * 100
            
            # 9. Convert data for javscript chart
            points = []
            for i in range(240):
                obj = {'x': float(wavelengths[i]), 'y': float(real_intensities[i])}
                points.append(obj)
            data = json.dumps({ 'data': points })

            # 10. Send data to client
            await websocket.send(data)
            # Wait 1 second
            await asyncio.sleep(1)
        
# Start server
start_server = websockets.serve(senddata, '127.0.0.1', 5678)
print('Started.')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
