from dataclasses import dataclass
from flask import Flask, Blueprint

from injector import inject
from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""

    app_handler: AppHandler

    # 使用dataclass这个装饰就可以省略下面的代码了
    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_router(self, app: Flask):
        """注册路由"""
        # 创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2. 将url与对应的控制器绑定
        bp.add_url_rule("/app", methods=["POST"], view_func=self.app_handler.create_app)
        bp.add_url_rule("/app/<uuid:id>", view_func=self.app_handler.get_app)
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule(
            "/apps/<uuid:app_id>/debug",
            methods=["POST"],
            view_func=self.app_handler.debug,
        )
        bp.add_url_rule(
            "/app/<uuid:id>", methods=["PUT"], view_func=self.app_handler.update_app
        )
        bp.add_url_rule(
            "/app/<uuid:id>", methods=["DELETE"], view_func=self.app_handler.delete_app
        )

        # 3.在应用上去注册蓝图
        app.register_blueprint(bp)
