from openai import OpenAI

client = OpenAI(
    api_key = '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'
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful vistual assistant named Jarvis skilled in tasks like alexa and google "},
        {
            "role": "user",
            "content": "What is coding ?"
        }
    ]
)

print(completion.choices[0].message.content)