from flask_migrate import Migrate
from pkg.sqlalchemy import SQLAlchemy
from injector import Injector

import dotenv
from .module import ExtensionModule
from internal.router import Router
from internal.server import Http
from config import Config


# 将环境变量添加到全局
dotenv.load_dotenv()

conf = Config()


# 依赖注入
injector = Injector([ExtensionModule])

app = Http(
    __name__,
    conf=conf,
    db=injector.get(SQLAlchemy),
    migrate=injector.get(Migrate),
    router=injector.get(Router),
)


if __name__ == "__main__":
    app.run(debug=True)
