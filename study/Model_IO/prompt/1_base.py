from datetime import datetime
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain_core.messages import AIMessage

# 定义模版
prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
print("PromptTemplate:", prompt)

# 方式1： format - 将模版直接变为可用的消息
print("PromptTemplate.format:", prompt.format(subject="程序员"))

prompt1 = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
# 方式2: 先用invoke变为PromptValue
# 通过to_string变为文本消息
# 通过to_messages变为聊天列表消息
prompt_value = prompt1.invoke({"subject": "程序员"})
print("PromptValue:", prompt_value)
print("PromptValue.to_string:", prompt_value.to_string())
print("PromptValue.to_messages:", prompt_value.to_messages())

# 创建一个 ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是我的私人助理，根据我的提问进行回复，当前时间为{now}"),
        #  消息占位符, 可能有其他的消息，但是不确定
        MessagesPlaceholder("chat_history"),
        HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话"),
    ]
).partial(now=datetime.now())

chat_prompt_value = chat_prompt.invoke(
    {
        "chat_history": [
            ("human", "我叫小王"),
            AIMessage("你好，我是小助理，有什么可以帮到你的！"),
        ],
        "subject": "程序员",
    }
)
print()
print("chat_prompt_value:", chat_prompt_value)
print("chat_prompt_value to str:", chat_prompt_value.to_string())
