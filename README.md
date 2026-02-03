

# flask-migrate
## 初始化
uv run flask init db
## 生成迁移脚本
uv run flask db migrate -m "create_table"
-m "create_table" 是给这个迁移写一个注释
生成的迁移脚本中有两个参数：
- upgrade(): 把迁移中的改动应用到数据库中
- downgrade(): 将改动撤销

# LangChain
## LangChain 框架本身由多个开源库组成（vO.2.1版本）：
- langchain-core：基础抽象和 LangChain 表达式语言。
- langchain-community：第三方集成以及合作伙伴包（如 langchain-openai、langchain-anthropic 等），一些集成已经进一步拆
分为自己的轻量级包，只依赖于 langchain-Core。
- langchain：构建应用程序认知架构的链、代理和检索策略。
- langgraph：通过将步骤构建为图中的边和节点，使用LLMs 构建健壮且有状态的多参与者应用程序。
- langserve：将 LangChain 链部署为 REST API。
- langsmith：一个开发平台，可以让你调试、测试、评估和监控 LLM 应用程序，并与LangChain 无缝衔接。
