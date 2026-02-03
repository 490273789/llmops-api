from datetime import datetime
from langchain.prompts import ChatPromptTemplate
import os
from langchain.chat_models import init_chat_model


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是聊天机器人，请回答用户的问题，现在时间是{now}"),
        ("human", "{query}"),
    ]
).partial(now=datetime.now())


llm = init_chat_model(
    model="deepseek-chat",
    api_base=os.getenv("DEEPSEEK_API_BASE"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# ai_message = llm.invoke(prompt.invoke({"query": "请讲一个冷笑话"}))
# print(f"ai_message: {ai_message.content}")

ai_messages = llm.batch(
    [
        prompt.invoke({"query": "你好，你是？"}),
        prompt.invoke({"query": "你好请讲一个关于程序员的笑话！"}),
    ]
)

for message in ai_messages:
    print(f"content: {message.content}")
    print("=" * 40)
