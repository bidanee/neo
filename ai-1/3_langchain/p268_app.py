from langchain.memory import ConversationBufferWindowMemory
# 여기서 k는 최근 대화중 기억할 갯수이다. 그래서 첫번째 대화가 안나온다.
memory = ConversationBufferWindowMemory(k=2, return_messages=True)
memory.save_context({"input": "안녕"},{"output": "무슨 일이야?"})
memory.save_context({"input": "집에 가고 싶어."},{"output": "나도"})
memory.save_context({"input": "밥이나 먹자"},{"output": "그게 나을듯싶다."})
print(memory.load_memory_variables({}))