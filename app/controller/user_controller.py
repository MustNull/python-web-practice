from .base_router import BaseRouter
from app.service import UserService as service
from pydantic import BaseModel


router = BaseRouter(prefix='/users')


class User(BaseModel):
    username: str
    password: str


@router.get('/')
def list(offset=0, limit=10):
    return service.list(limit=limit, offset=offset)


@router.post('/')
def create(user: User):
    return service.create(**user.dict())


@router.put('/{mid}')
def update_by_id(mid: int, user: User):
    return service.update_by_id(mid, **user.dict())


@router.delete('/{mid}')
def delete_by_id(mid: int):
    return service.delete_by_id(mid)
