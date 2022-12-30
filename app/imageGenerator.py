import openai

openai.api_key = ""

def generate_image(prompt):

    return openai.Image.create(prompt=prompt, n=2, size="1024x1024")["data"][0]["url"]