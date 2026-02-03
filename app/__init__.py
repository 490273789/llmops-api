# 文件夹下有__init__.py说明这个文件是一个package

from app.http import app

__all__ = ["app"]
