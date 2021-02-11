from app.model.base_model import BaseModel


class BaseDao:
    model = BaseModel

    @classmethod
    def get_by_id(cls, mid):
        # ToDo:不存在时抛出自定义异常
        return cls.model.get_by_id(mid)

    @classmethod
    def create(cls, **kwargs):
        return cls.model.create(**kwargs)

    @classmethod
    def update_by_id(cls, mid, **kwargs):
        cls.model.update(**kwargs).where(cls.model.id == mid)
        return cls.get_by_id(mid)

    @classmethod
    def soft_delete_by_id(cls, mid):
        return cls.update_by_id(mid, deleted=True)

    @classmethod
    def delete_by_id(cls, mid):
        return cls.model.delete_by_id(mid)

    @classmethod
    def query(cls, _conditions=(True,), deleted=False, **kwargs):
        conditions = [c for c in _conditions]
        conditions.append(cls.model.deleted == deleted)
        for k, v in kwargs.items():
            conditions.append(getattr(cls.model, k) == v)
        return cls.model.select().where(*conditions)
