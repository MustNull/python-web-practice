from enum import Enum
from config import PRODUCTION, DEVELOPMENT


class EnvMode(str, Enum):
    DEVELOPMENT = DEVELOPMENT
    PRODUCTION = PRODUCTION
