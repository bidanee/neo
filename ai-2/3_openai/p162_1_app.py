import openai
import json

messages = [
  {"role" : "user", "content" : "너의 이름은?"},
]

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages,
  max_tokens=100,
  temperature=0.7,
  n=1
)

print('-' * 50)
message = response.choices[0].message
print(json.dumps(message,ensure_ascii=False))