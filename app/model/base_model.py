from peewee import Model, BooleanField
from db import db


class BaseModel(Model):
    deleted = BooleanField(default=False)

    class Meta:
        database = db

    @classmethod
    def should_create_table(cls):
        return not getattr(cls, 'abstract', None) and cls != BaseModel
