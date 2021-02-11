from config import CONFIG
from peewee import PostgresqlDatabase


connect_parameters = CONFIG.app.database.connect_parameters


def get_db(**kwargs):
    return PostgresqlDatabase(**kwargs)


db = get_db(**connect_parameters)
