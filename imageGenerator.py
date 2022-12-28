import openai

openai.api_key = "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"

def generate_image(prompt):

    return openai.Image.create(prompt=prompt, n=2, size="1024x1024")["data"][0]["url"]