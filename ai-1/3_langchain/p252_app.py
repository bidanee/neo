from langchain.agents import load_tools
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent

tools = load_tools(
  tool_names = ["serpapi","llm-math"],
  llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature = 0
  )
)

memory = ConversationBufferWindowMemory(
  memory_key = "chat_history",
  k = 5,
  return_messages = True
)

agent = initialize_agent(
  agent = "conversational-react-description",
  llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature = 0
  ),
  tools = tools,
  memory = memory,
  verbose = True
)

print(agent.run("집에 가고싶습니다."))
print('-' * 50)

print(agent.run("저는 애완동물을 안키웁니다."))
print('-' * 50)

print(agent.run("애완동물을 추천해주세요."))
print('-' * 50)

print(agent.run("123 *₩ 4를 계산기로 계산해주세요."))
print('-' * 50)

print(agent.run("오늘 한국의 서울 날씨를 말해주세요."))
print('-' * 50)

