from google import genai

client = genai.Client(api_key="")

while True:
  question = input("What is your question? \n")
  prompt = f'''
        System: You are a gamer with no social skills. The user is someone who randomly came up to you to ask a question. Respond in how an asocial person would answer.
        User: {question}
  '''

  response = client.models.generate_content(
      model="gemini-3-pro",
      contents=prompt
)

print(response.text)
