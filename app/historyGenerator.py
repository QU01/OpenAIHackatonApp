import openai

openai.api_key = "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"

def generate_history(prompt):

    prompt = "Generate a brief history about " + prompt

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=512)

    return response["choices"][0]["text"].encode("utf-8").decode()