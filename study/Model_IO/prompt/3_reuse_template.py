from langchain_core.prompts import PromptTemplate, PipelinePromptTemplate
from langchain.chains.sequential import SimpleSequentialChain

final_prompt = PromptTemplate.from_template("""
{instruction}
{example}
{start}""")

instruction_prompt = PromptTemplate.from_template("你正在模拟{person}")

example_prompt = PromptTemplate.from_template("""
下面是一个交互的例子：

Q: {example_q}  
A: {example_a}          
""")

start_prompt = PromptTemplate.from_template("""现在你是一个真实的人，请回答用户问题：

Q: {input}
A:""")


pipeline_steps = [
    ("instruction", instruction_prompt),
    ("example", example_prompt),
    ("start", start_prompt),
]


pipeline_prompt = PipelinePromptTemplate(
    final_prompt=final_prompt,
    pipeline_prompts=pipeline_steps,
)


print(
    "pipeline_prompt (deprecated API):",
    pipeline_prompt.invoke(
        {
            "person": "Ethan",
            "example_q": "你是谁？",
            "example_a": "我是Ethan",
            "input": "Who are you?",
        }
    ).to_string(),
)


def render_prompt_sequence(
    final_prompt: PromptTemplate,
    pipeline_prompts: list[tuple[str, PromptTemplate]],
    initial_inputs: dict,
) -> str:
    """Replicate the deprecated pipeline behavior with explicit chaining."""
    context = dict(initial_inputs)
    for name, prompt in pipeline_prompts:
        prompt_inputs = {key: context[key] for key in prompt.input_variables}
        context[name] = prompt.format(**prompt_inputs)
    final_inputs = {key: context[key] for key in final_prompt.input_variables}
    return final_prompt.format(**final_inputs)


print(
    "pipeline_prompt (manual chaining):",
    render_prompt_sequence(
        final_prompt=final_prompt,
        pipeline_prompts=pipeline_steps,
        initial_inputs={
            "person": "Ethan",
            "example_q": "你是谁？",
            "example_a": "我是Ethan",
            "input": "Who are you?",
        },
    ),
)


my_input = {
    "person": "Ethan",
    "example_q": "你是谁？",
    "example_a": "我是Ethan",
    "input": "Who are you?",
}
for name, prompt in pipeline_steps:
    my_input[name] = prompt.invoke(my_input).to_string()


my_output = final_prompt.invoke(my_input).to_string()
print()
print("my_output:", my_output)

SimpleSequentialChain
