from teste_flet02 import db, Data
from peewee import *


db.connect()
db.create_tables([Data], safe=True)



for _ in Data.select():
    print(_.id, _.nome)