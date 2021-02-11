from peewee_migrate import Router
from db import db
from config import CONFIG
import os
from app.model.base_model import BaseModel


migrate_direcotry = os.path.abspath(os.path.relpath(
    CONFIG.app.database.migrate_directory, CONFIG.ROOT_PATH))

router = Router(db, migrate_direcotry)


def create(name):
    result = router.create(name)
    router.logger.info(os.path.join(migrate_direcotry, result + '.py'))
    return result


def run(name=None):
    if name is None:
        return router.run()
    return router.run(name)


def rollback(name):
    return router.rollback(name)


def __get_all_models():
    result = []
    for cls in BaseModel.__subclasses__():
        if cls.should_create_table():
            result.append(cls)
    return result


def initdb():
    models = __get_all_models()
    exists_models = [m for m in models if m.table_exists()]
    drop_tables(exists_models)
    db.create_tables(models)
    print('success create tables', models)


def drop_tables(models=None):
    if models is None:
        models = __get_all_models()
    db.drop_tables(models)
    print('success drop tables', models)
