from .base_service import BaseService
from app.dao import UserDao


class UserService(BaseService):
    dao = UserDao
