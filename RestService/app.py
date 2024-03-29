from flask import Flask
from routes import app_
from flask_cors import CORS
from playhouse.postgres_ext import PostgresqlExtDatabase
from models import database_proxy, create_tables
import os, time
from argparse import ArgumentParser

database = PostgresqlExtDatabase('remotelab', user='postgres', password='postgres', host='localhost')
database_proxy.initialize(database)
create_tables()
app = Flask(__name__)
CORS(app)
app.register_blueprint(app_)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-host')
    parser.add_argument('-port')
    args = parser.parse_args()
    host = args.host
    port = int(args.port)

    app.run(host = host, port = port, debug = True)
