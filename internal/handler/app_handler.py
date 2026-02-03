import uuid
from dataclasses import dataclass
from injector import inject
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppsService
from pkg.response import success_json, validate_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    app_service: AppsService

    def create_app(self):
        app = self.app_service.create_app()
        return success_message(f"应用已成功创建，应用Id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用name为{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"更新后名字是{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"删除成功，删除id为{app.id}")

    def debug(self, app_id: uuid.UUID):
        print(f"uuid: {app_id}")
        """聊天窗口"""
        # 1. 验证请求参数 post
        req = CompletionReq()
        if not req.validate():
            return validate_json(errors=req.errors)
        # 2. 创建客户端
        client = init_chat_model(model="deepseek-chat", model_provider="deepseek")
        # 3. 得到请求响应，将响应返回给前端
        prompt = ChatPromptTemplate.from_template("{query}")
        # 4. 创建输出解析器
        parser = StrOutputParser()
        # 5. 创建调用链
        chain = prompt | client | parser

        content = chain.invoke({"query": req.query.data})

        return success_json(data={"content": content})

    def ping(self):
        raise FailException(message="数据未找到")
        # return {"ping": "pong"}
