# 字符串拼接
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# 文本提示模版
# 模版拼接的第一个模版必须是PromptTemplate，这个方法重写了"+"的规则
prompt = (
    PromptTemplate.from_template("请讲一个关于{subject}的笑话")
    + ",让我开心一下。"
    + "\n使用{language}语言"
)
print(f"prompt: {prompt}")
print("PromptValue:", prompt.invoke({"subject": "java", "language": "英语"}))

# 消息模版
system_chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是我的私人助理,你叫{name}")]
)
human_chat_prompt = ChatPromptTemplate.from_messages([("human", "{query}")])

chat_prompt = system_chat_prompt + human_chat_prompt
print(f"chat_prompt: {chat_prompt}")
print("PromptValue:", chat_prompt.invoke({"name": "Shown", "query": "谁最帅？"}))
