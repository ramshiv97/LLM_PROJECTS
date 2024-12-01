import openai

openai.api_key = "your_openai_api_key"

def translate_query(user_query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate this into a database query:\n'{user_query}'",
        max_tokens=150
    )
    return response.choices[0].text.strip()
