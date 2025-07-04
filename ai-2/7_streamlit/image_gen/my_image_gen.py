# import openai
# import os
# import textwrap

# def translate_text_to_image(text):
#   user_content = f'Translate the following Korean sentence into English: \n"{text}"'
#   message = [
#     {"role":"user", "content":user_content}
#   ]
  
#   response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=message,
#     max_tokens=500,
#     temperature=0.8,
#     n = 1
#   )

#   assistant_reply = response.choices[0].message['content']
  
#   return assistant_reply

# def generate_text_for_image(text):
#   user_content = f'Translate the following in 1000 characters to create an Image. \n"{text}"'
#   message = [
#     {"role":"user", "content":user_content}
#   ]
  
#   response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=message,
#     max_tokens=500,
#     temperature=0.8,
#     n = 1
#   )
  
#   assistant_reply = response['choices'][0]['message']['content']
  
#   return assistant_reply

# def genrate_image_from_text(text_for_image, image_num=1, image_size="512x512"):
#   shorten_test_for_image = textwrap.shorten(text_for_image, width=1000)
  
#   response = openai.Image.create(
#     prompt=shorten_test_for_image,
#     n=image_num,
#     size=image_size
#   )
  
#   image_urls = []
#   for data in response['data']:
#     image_url = data['url']
#     image_urls.append(image_url)
#   return image_urls

import openai
import os
import textwrap

def translate_text_for_image(text):
    user_content = f'Translate the following Korean sentence into English: \n"{text}"'
    messgage = [
        {"role": "user", "content": user_content}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messgage,
        max_tokens=100,
        temperature=0.8,
        n = 1
    )

    assistant_reply = response['choices'][0]['message']['content']

    return assistant_reply

def generate_text_for_image(text):
    user_content = f'Translate the following in 1000 characters to create an Image. \n"{text}"'

    message = [
        {"role": "user", "content": user_content}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        max_tokens=500,
        temperature=0.8,
        n = 1
    )

    assistant_reply = response.choices[0].message['content']

    return assistant_reply

def generate_image_from_text(text_for_image, image_num=1, image_size="512x512"):
    shorten_text_for_image = textwrap.shorten(text_for_image, 1000)

    response = openai.Image.create(
        prompt=shorten_text_for_image,
        n=image_num,
        size=image_size
    )

    image_urls = []
    for data in response['data']:
        image_url = data['url']
        image_urls.append(image_url)
    return image_urls