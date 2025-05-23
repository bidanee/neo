import openai

with open("/neo/ai-1/1_openai/2_image/image_fixed.png", "rb") as image_file, \
     open("/neo/ai-1/1_openai/2_image/mask_fixed.png", "rb") as mask_file:

    response = openai.Image.create_edit(
        image=image_file,
        mask=mask_file,
        prompt="many apples in cardboard box",
        n=1,
        size="512x512",
    )

print(response["data"][0]["url"])
