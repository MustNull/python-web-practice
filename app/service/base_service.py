from app.dao.base_dao import BaseDao


class BaseService:
    dao = BaseDao

    @classmethod
    def create(cls, **kwargs):
        return cls.dao.create(**kwargs)

    @classmethod
    def get_by_id(cls, mid):
        return cls.dao.get_by_id(mid)

    @classmethod
    def update_by_id(cls, mid, **kwargs):
        cls.get_by_id(mid)
        return cls.dao.update_by_id(mid, **kwargs)

    @classmethod
    def delete_by_id(cls, mid):
        result = cls.get_by_id(mid)
        cls.dao.delete_by_id(mid)
        return result

    @classmethod
    def soft_delete_by_id(cls, mid):
        return cls.dao.soft_delete_by_id(mid)

    @classmethod
    def list(cls):
        result = cls.dao.query()
        return [u for u in result]
