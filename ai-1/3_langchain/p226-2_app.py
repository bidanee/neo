from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

examples = [
    {"input": "明るい", "output": "暗い"},
    {"input": "おもしろい", "output": "つまらない"},
]

# 예시 템플릿 (출력 뒤에 \n 없앰, 마지막에 빈 줄 안 넣음)
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="入力: {input}\n出力: {output}"
)

prompt_from_string_examples = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="모든 입력에 대한 반의어를 입력하세요.",
    suffix="입력: {adjective}",
    input_variables=["adjective"],
    example_separator="\n\n",
)

chat_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
message = "큰"
prompt = prompt_from_string_examples.format(adjective=message)

result = chat_llm([HumanMessage(content=prompt)])

print("생성된 프롬프트:")
print(prompt)
print(result.content)
