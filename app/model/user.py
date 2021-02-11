from .base_model import BaseModel
from peewee import CharField


class User(BaseModel):
    username = CharField()
    password = CharField()
