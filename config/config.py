import os

from .default_config import DEFAULT_CONFIG


def _get_env(key: str):
    """从环境变量中获取默认配置项"""
    # 第二个参数的作用，如果获取到相应的key，则返回获取到的值，如果没有获取到则返回第二个参数，第二个参数是个默认值
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str):
    """从环境变量中获取布尔类型的配置项"""
    value: str = _get_env(key)
    return value.lower() == "true" if value is not None else False


class Config:
    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = False
        # 配置数据库
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
