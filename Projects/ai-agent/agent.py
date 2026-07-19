from openai import OpenAI
from config import OPENROUTER_API_KEY

from tools.calculator import *
from tools.datetime_tool import get_datetime
from tools.summarizer import summarize
from tools.fact_generator import random_fact


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


print("🤖 AI Agent Started")
print("Type 'exit' to quit.")
print("Type 'history' to view conversation history.\n")


memory = []


while True:

    user = input("You: ")

    # Display conversation history
    if user.lower() == "history":

        print("\nConversation History\n")

        if len(memory) == 0:
            print("No conversation yet.\n")

        else:
            for msg in memory:
                print(msg)

        continue


    # Exit application
    if user.lower() == "exit":

        print("Goodbye!")
        break


    # Previous conversation context
    history_text = "\n".join(memory)


    # LLM prompt
    prompt = f"""
You are an AI Agent.

Previous Conversation:
{history_text}

Current User Request:
{user}

Available tools:

calculator
datetime
summarizer
fact

Reply ONLY with one word.
"""


    # Ask LLM to select a tool
    response = client.chat.completions.create(
        model="tencent/hy3:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    # Save user message in memory
    memory.append(f"User: {user}")


    # Keep only the last 5 messages
    if len(memory) > 5:
        memory.pop(0)


    tool = response.choices[0].message.content.strip().lower()

    print("Selected Tool:", tool)


    # Date & Time Tool
    if tool == "datetime":

        dt = get_datetime()

        print("Date:", dt["date"])
        print("Time:", dt["time"])


    # Random Fact Tool
    elif tool == "fact":

        print(random_fact())


    # Summarizer Tool
    elif tool == "summarizer":

        text = input("Enter paragraph:\n")

        print(summarize(text))


    # Calculator Tool
    elif tool == "calculator":

        a = float(input("First Number: "))
        b = float(input("Second Number: "))

        op = input("Operation (+,-,*,/): ")


        if op == "+":

            print(add(a, b))


        elif op == "-":

            print(subtract(a, b))


        elif op == "*":

            print(multiply(a, b))


        elif op == "/":

            print(divide(a, b))


        else:

            print("Invalid Operation")


    else:

        print("I don't know which tool to use.")