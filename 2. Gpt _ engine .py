import openai

openai.api_key = "YOUR_OPENAI_KEY"

def get_explanation(code):
    prompt = f"You are a helpful AI that explains Python code like a human teacher.\nCode:\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']