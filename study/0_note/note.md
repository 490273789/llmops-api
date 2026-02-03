# Prompt Template 知识整理

## 概述

在 LangChain 中，Prompt Template（提示模板）涵盖了多个子组件，包括：
- **角色提示模板** (SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate)
- **消息占位符** (MessagePlaceholder)
- **文本提示模板** (PromptTemplate, ChatPromptTemplate)
- **聊天消息提示模板**
- **提示、消息** 等

## Prompt Template 运行流程

### 1. 角色提示模板（Message Prompt Templates）

提供了三种角色类型的提示模板：

- **SystemMessagePromptTemplate** - 系统消息提示模板
- **HumanMessagePromptTemplate** - 人类消息提示模板  
- **AIMessagePromptTemplate** - AI消息提示模板
- **MessagePlaceholder** - 消息占位符

### 2. 提示模板类型（Prompt Template Types）

提示模板主要分为两大类：

#### PromptTemplate (文本提示模板)
- 用于生成文本格式的提示
- 适用于简单的文本场景

#### ChatPromptTemplate (聊天消息提示模板)
- 用于生成聊天消息格式的提示
- 支持多轮对话场景

### 3. 提示值（PromptValue）

通过 `invoke()` 方法调用提示模板后，会生成 **PromptValue（提示值）**对象。

PromptValue 可以转换为两种消息类型：

- **to_string()** → 转换为**文本消息**
- **to_messages()** → 转换为 **List[BaseMessage] 聊天消息列表**

### 4. 部分格式化（Partial Formatting）

通过 `partial()` 方法可以实现**部分格式化部分变量**，这允许：
- 预先填充某些变量
- 延迟填充其他变量
- 创建可重用的模板


## 使用场景

1. **角色定义**：使用不同的消息提示模板定义系统、用户和AI的角色
2. **模板复用**：通过提示模板实现提示词的标准化和复用
3. **动态生成**：使用变量和占位符动态生成提示内容
4. **格式转换**：根据需要将提示值转换为文本或消息列表格式
5. **部分填充**：使用 partial() 方法预先填充部分变量，提高灵活性

## 关键方法

- `format()` - 格式化模板，填充所有变量
- `invoke()` - 调用模板，生成 PromptValue 对象
- `partial()` - 部分格式化，预填充部分变量
- `to_string()` - 将 PromptValue 转换为字符串
- `to_messages()` - 将 PromptValue 转换为消息列表

