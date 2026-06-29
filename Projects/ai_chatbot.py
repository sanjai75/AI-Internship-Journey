from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY"
)

print("=" * 50)
print("      AI PROGRAMMING ASSISTANT")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nWelcome {name}!")
print("Ask me anything about programming.")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print(f"\nGoodbye {name}!")
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("\nAI:")
    print(response.choices[0].message.content)
    print("-" * 50)