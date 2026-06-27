import google.generativeai as genai

# Paste your Gemini API Key here
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-2.0-flash")

print("=" * 50)
print("        AI PROGRAMMING ASSISTANT")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nWelcome {name}!")
print("Ask me anything about programming.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print(f"\nGoodbye {name}! Have a great day!")
        break

    try:
        response = model.generate_content(user_input)

        print("\nAI:")
        print(response.text)
        print("\n" + "-" * 50 + "\n")

    except Exception as e:
        print("\nError:", e)
        print("\n" + "-" * 50 + "\n")