import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

results = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Explain the benefits of learning ChatGPT Prompt Engineering."}
  ]
)

print(results.choices[0].message.content)


