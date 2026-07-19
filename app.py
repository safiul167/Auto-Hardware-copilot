from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
)

print("=== Automotive Hardware AI Copilot ===")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[
            {"role": "system", "content": "You are an Automotive Hardware Design expert."},
            {"role": "user", "content": question}
        ]
    )

    print("\nCopilot:")
    print(response.choices[0].message.content)
    print("-" * 50)