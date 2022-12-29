import openai

openai.api_key = "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"

def generate_image(prompt):

    return openai.Image.create(prompt=prompt, n=2, size="1024x1024")["data"][0]["url"]