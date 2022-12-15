import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):

    return openai.Image.create(prompt=prompt, n=2, size="1024x1024")["data"][0]["url"]