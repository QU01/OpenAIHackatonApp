import openai

openai.api_key = "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"

def generate_history(prompt):

    prompt = "Generate a brief history about " + prompt

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=256)

    return response["choices"][0]["text"].encode("utf-8").decode()