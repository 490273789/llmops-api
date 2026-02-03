from datetime import datetime
from langchain.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是聊天机器人，请回答用户的问题，现在时间是{now}"),
        ("human", "{query}"),
    ]
).partial(now=datetime.now())


llm = ChatDeepSeek(model="deepseek-chat")

response = llm.stream(prompt.invoke({"query": "请讲一个冷笑话"}))


for chunk in response:
    print(chunk.content, flush=True, end="")
