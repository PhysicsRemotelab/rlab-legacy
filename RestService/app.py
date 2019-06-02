from flask import Flask
from routes import app_
from flask_cors import CORS
from playhouse.postgres_ext import PostgresqlExtDatabase
from models import database_proxy, create_tables
import os, time

database = PostgresqlExtDatabase('remotelab', user='postgres', password='postgres', host='localhost')
database_proxy.initialize(database)
create_tables()
app = Flask(__name__)
CORS(app)
app.register_blueprint(app_)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3000, debug = True)
