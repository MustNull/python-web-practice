from .base_dao import BaseDao
from app.model import User


class UserDao(BaseDao):
    model = User
