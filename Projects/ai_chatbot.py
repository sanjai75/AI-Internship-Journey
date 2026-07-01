from openai import OpenAI
from datetime import datetime
import os
import time

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY"   # Replace with your API key while testing
)

print("=" * 55)
print("      AI PROGRAMMING ASSISTANT")
print("=" * 55)

name = input("Enter your name: ")

print(f"\nWelcome {name}!")
print("Ask me anything about Programming.")
print("Type /help to see commands.\n")

conversation = []

while True:

    user_input = input("You: ")

    # Exit
    if user_input.lower() == "exit":
        print(f"\nGoodbye {name}! Have a great day!")
        break

    # Help
    if user_input.lower() == "/help":
        print("\nAvailable Commands")
        print("----------------------------")
        print("/help   - Show commands")
        print("/clear  - Clear screen")
        print("exit    - Exit chatbot")
        print("----------------------------\n")
        continue

    # Clear Screen
    if user_input.lower() == "/clear":
        os.system("cls" if os.name == "nt" else "clear")
        print("Screen Cleared!\n")
        continue

    # Current Date & Time
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print("\nAI is thinking...")
    time.sleep(1)

    try:

        conversation.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=conversation
        )

        ai_reply = response.choices[0].message.content

        conversation.append({
            "role": "assistant",
            "content": ai_reply
        })

        print(f"\n[{current_time}]")
        print("AI:")
        print(ai_reply)

        # Save Chat History
        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"\n[{current_time}]\n")
            file.write(f"You: {user_input}\n")
            file.write(f"AI: {ai_reply}\n")
            file.write("-" * 50 + "\n")

        print("-" * 55)

    except Exception as e:
        print("\nError:")
        print("Unable to get response from AI.")
        print("Reason:", e)
        print("Please try again after a few seconds.")
        print("-" * 55)