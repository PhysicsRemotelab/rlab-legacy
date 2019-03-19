import datetime
from playhouse.postgres_ext import JSONField
from peewee import Proxy, Model, PrimaryKeyField, CharField, DateField, BooleanField, ForeignKeyField

database_proxy = Proxy()

class BaseModel(Model):
    class Meta:
        database = database_proxy

class User(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=1000)
    code = CharField(max_length=1000)
    created = DateField(default=datetime.datetime.now)
    updated = DateField(default=datetime.datetime.now)

class Lab(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=1000)
    description = CharField(max_length=1000)
    taken = BooleanField(default=False)
    seo = CharField(max_length=1000)
    created = DateField(default=datetime.datetime.now)
    updated = DateField(default=datetime.datetime.now)

class Measurement(BaseModel):
    id = PrimaryKeyField(null=False)
    lab_id = ForeignKeyField(Lab, backref='measurements')
    user_id = ForeignKeyField(User, backref='measurements')
    results = JSONField()
    created = DateField(default=datetime.datetime.now)
    updated = DateField(default=datetime.datetime.now)

def create_tables():
    database_proxy.connect()
    database_proxy.create_tables([User, Lab, Measurement])
