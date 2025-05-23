import openai
# 이미지 생성

prompt = 'Cat dancing on the Car'

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512",
)

image_url = response['data'][0]['url']
print(image_url)