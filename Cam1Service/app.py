from importlib import import_module
import os
from flask import Flask, render_template, Response
from flask_cors import CORS

# import camera driver
from camera0 import BaseCamera

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed0')
def video_feed0():
    """Video streaming route. Put this in the src attribute of an img tag."""
    cam = BaseCamera(0)
    return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    cam = BaseCamera(1)
    return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(port=4001, threaded=True)
