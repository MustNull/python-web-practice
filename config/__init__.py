import yaml
import os


PRODUCTION = 'production'
DEVELOPMENT = 'development'
LOCAL_KEY = '.local'
ENV_MODE = os.environ.get('ENV', DEVELOPMENT)
CONFIG_DIR_PATH = os.path.dirname(__file__)
ROOT_PATH = os.path.dirname(CONFIG_DIR_PATH)


class ConfigDict(dict):
    def __getattr__(self, key):
        result = self.__getitem__(key)
        if isinstance(result, dict):
            return ConfigDict(result)
        return result

    def __setattr__(self, key, value):
        # ToDo 自定义异常
        self[key] = value


class Config(ConfigDict):
    ENV_MODE = ENV_MODE
    ROOT_PATH = ROOT_PATH

    def __init__(self):
        super().__init__()
        local_config = {}
        for key, config in self.__load_all_yml():
            # 如果对应模式不存在,默认读取开发模式配置
            if key == LOCAL_KEY:
                local_config = config
                continue
            self[key] = config
        self.update_local(local_config)

    def update_local(self, local_config):
        for keys, v in self.__iterall_keys_and_value(local_config):
            config = self
            for k in keys[:-1]:
                config = config[k]
            config[keys[-1]] = v

    @classmethod
    def __iterall_keys_and_value(cls, config):
        for k, v in config.items():
            if isinstance(v, dict):
                for _ks, _v in cls.__iterall_keys_and_value(v):
                    _ks.insert(0, k)
                    yield _ks, _v
            else:
                yield [k], v

    @classmethod
    def __load_all_yml(cls, dir_path=CONFIG_DIR_PATH):
        for file in os.listdir(dir_path):
            if file.endswith('.yml'):
                file_path = os.path.join(dir_path, file)
                yield file[:-4], cls.__load_config_by_yml(file_path)

    @classmethod
    def __load_config_by_yml(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            result = yaml.safe_load(f)
        result = result or {}
        return result


CONFIG = Config()
