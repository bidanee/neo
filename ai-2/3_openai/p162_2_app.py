import openai
import json

messages = [
  {"role" : "user", "content" : "한글은 누가 만들었나요?"},
]

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages,
  max_tokens=100,
  temperature=0.7,
  n=2
)

print("응답 개수 : ", len(response['choices']))