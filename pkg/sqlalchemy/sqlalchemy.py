from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    """重写Flask-SQLAlchemy"""

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


"""
正常流程：

执行 yield 之前的代码（这里是 try）
执行 with 块中的数据库操作
如果一切正常，自动调用 self.session.commit() 提交事务
异常处理：

如果 with 块中的代码抛出任何异常
自动调用 self.session.rollback() 回滚事务
重新抛出异常，让上层代码处理
"""
# 不使用 auto_commit（传统方式）
# try:
#     db.session.add(new_user)
#     db.session.commit()
# except Exception as e:
#     db.session.rollback()
#     raise e

# 使用 auto_commit（简化方式）
# with db.auto_commit():
#     db.session.add(new_user)
# 自动提交或回滚

"""
@contextmanager 装饰器
这是 Python 标准库 contextlib 模块提供的装饰器，用于将生成器函数转换为上下文管理器。
它让你可以用简单的生成器函数来实现上下文管理器，
而不需要定义一个完整的类（实现 __enter__ 和 __exit__ 方法）。
1.进入阶段（with 语句开始）：
    执行 yield 之前的代码
    这里是 try: 语句块的开始

2.主体执行（with 块内的代码）：
    执行 yield，暂停函数执行
    控制权交给 with 块内的代码

3.退出阶段（with 语句结束）：
    如果正常执行：继续 yield 之后的代码 → commit()
    如果有异常：进入 except 块 → rollback() 并重新抛出异常
"""
# 不使用装饰器（传统类方式）：
# class AutoCommit:
#     def __init__(self, session):
#         self.session = session

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.session.commit()
#         else:
#             self.session.rollback()
#         return False
