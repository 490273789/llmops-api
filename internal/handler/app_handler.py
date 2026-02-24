import uuid
from dataclasses import dataclass

from injector import inject
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppsService
from pkg.response import success_json, success_message, validate_json


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

        llm = init_chat_model(model="deepseek-chat")
        config = {"configurable": {"thread_id": str(app_id)}}

        checkpoint = InMemorySaver()
        agent = create_agent(
            model=llm,
            middleware=[
                SummarizationMiddleware(
                    model=llm,
                    trigger=("tokens", 400),
                    keep=("messages", 10),
                    summary_prompt="",
                )
            ],
            checkpointer=checkpoint,
            system_prompt="你是一个强大的聊天机器人，能根据用户的提问回复对应的问题",
            # response_format=ToolStrategy(ContractInfo)
        )
        content = agent.invoke(
            {"messages": [{"role": "user", "content": req.query.data}]}, config=config
        )
        return success_json(data={"content": content["messages"][-1].content})

    def ping(self):
        raise FailException(message="数据未找到")
        # return {"ping": "pong"}
