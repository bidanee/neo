from langchain.memory import ConversationTokenBufferMemory
from langchain.chat_models import ChatOpenAI

memory = ConversationTokenBufferMemory(
  llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature = 0
  ),
  max_token_limit = 50,
  return_messages = True
)

memory.save_context({"input": "안녕"},{"output": "무슨 일이야?"})
memory.save_context({"input": "집에 가고 싶어."},{"output": "나도"})
memory.save_context({"input": "밥이나 먹자"},{"output": "그게 나을듯싶다."})

print(memory.load_memory_variables({}))