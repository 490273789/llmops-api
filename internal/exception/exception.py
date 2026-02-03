from dataclasses import field
from typing import Any
from pkg.response import HttpCode


class CustomException(Exception):
    """基础自定义异常信息"""

    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    """通用异常失败"""

    pass


class NotFoundException(CustomException):
    """未找到数据异常"""

    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    """未授权数据异常"""

    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    """没权限数据异常"""

    code = HttpCode.FORBIDDEN


class ValidateErrorException(CustomException):
    """数据验证异常"""

    code = HttpCode.VALIDATE_ERROR
