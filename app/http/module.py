from flask_migrate import Migrate
from pkg.sqlalchemy import SQLAlchemy
from injector import Binder, Module
from internal.extension import db, migrate


class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
