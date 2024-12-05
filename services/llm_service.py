import openai

# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = "give your api key here"

def translate_query(user_query):
    print("user_query: " + user_query)

    try:
        # Using ChatCompletion API for newer models
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you prefer
            messages=[
                {"role": "system", "content": "You are a SQL translator."},
                {"role": "user", "content": f"Translate this into a SQL query:\n'{user_query}'"}
            ],
            max_tokens=150,
            temperature=0.5
        )

        print("Response received from OpenAI:", response)
        # Extract and return the generated SQL query
        return response.choices[0].message["content"].strip()
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    user_query = "Show me the names of all employees in the 'Sales' department."
    sql_query = translate_query(user_query)
    if sql_query:
        print(f"Generated SQL Query:\n{sql_query}")
    else:
        print("Failed to generate the query.")