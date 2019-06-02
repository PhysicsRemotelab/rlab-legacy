from importlib import import_module
from flask import Flask, Response
from flask_cors import CORS
from camera import BaseCamera
from argparse import ArgumentParser

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
        return Response('Camera service running')

def gen(camera):
        while True:
                frame = camera.get_frame()
                yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed/')
def video_feed():
        index = app.config['camera']
        cam = BaseCamera(index)
        return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
        # Get port number from command line
        parser = ArgumentParser()
        parser.add_argument('-port')
        parser.add_argument('-camera')
        args = parser.parse_args()

        # Get camera id from command line
        app.config['camera'] = int(args.camera)

        app.run(port = int(args.port), threaded=True)
