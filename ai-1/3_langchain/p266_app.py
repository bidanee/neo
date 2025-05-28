from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("집에가고싶다.")
memory.chat_memory.add_ai_message("언제 집에 갈 수 있을까?")
memory.chat_memory.add_user_message("나도모르지.")
memory.chat_memory.add_ai_message("생각좀 해봐바")
memory.chat_memory.add_user_message("끝나야 가지")
memory.chat_memory.add_ai_message("그르킨 하지.")

print(memory.load_memory_variables({}))