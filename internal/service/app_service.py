from dataclasses import dataclass
import uuid
from pkg.sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App


@inject
@dataclass
class AppsService:
    """应用服务逻辑"""

    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.auto_commit():
            app = App(
                name="测试机器人",
                account_id=uuid.uuid4(),
                icon="",
                description="这是一个简单的聊天机器人",
            )
            self.db.session.add(app)
        return app

    def get_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return app

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "机器人2"

        return app

    def delete_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)

        return app
