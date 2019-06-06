from flask import Flask, Response
from argparse import ArgumentParser

app = Flask(__name__)

@app.route('/')
def index():
        return Response('Test service is running')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-host')
    parser.add_argument('-port')
    args = parser.parse_args()
    host = args.host
    port = int(args.port)

    app.run(host = host, port = port, debug = True)
