import os
from flask import Flask
from flask_migrate import Migrate
from pkg.sqlalchemy import SQLAlchemy

from internal.exception import CustomException
from internal.router import Router
from config import Config
from pkg.response import json, HttpCode, Response
from flask_cors import CORS


# 应用相关的http配置
class Http(Flask):
    """Http 服务引擎"""

    def __init__(
        self,
        *args,
        conf: Config,
        db: SQLAlchemy,
        migrate: Migrate,
        router: Router,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        # 初始化应用配置
        self.config.from_object(conf)

        # 注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 初始化Flask扩展
        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")

        # 解决后端跨域问题
        CORS(
            self,
            resources={
                r"/*": {
                    "origin": "*",
                    "supports_credentials": True,
                    "methods": ["GET", "POST"],
                    "allow_headers": ["Content-Type"],
                }
            },
        )
        # 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        print("异常：", error)
        # 如果是自定义异常，提取code以及message信息
        if isinstance(error, CustomException):
            return json(
                Response(
                    code=error.code,
                    message=error.message,
                    data=error.data if error.data is not None else {},
                )
            )

        # 如果不是自定义异常，则有可能是程序或数据库抛出的异常，设置为fail状态吗
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(code=HttpCode.FAIL, message=str(error), data={}))
