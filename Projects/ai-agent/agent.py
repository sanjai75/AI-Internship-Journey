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
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    prompt = f"""
You are an AI Agent.

Available tools:

1. calculator
2. datetime
3. summarizer
4. fact

Reply ONLY with one word.

calculator
datetime
summarizer
fact

User Request:
{user}
"""

    response = client.chat.completions.create(
        model="tencent/hy3:free",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    tool = response.choices[0].message.content.strip().lower()

    print("Selected Tool:", tool)

    if tool == "datetime":

        dt = get_datetime()

        print("Date:", dt["date"])
        print("Time:", dt["time"])

    elif tool == "fact":

        print(random_fact())

    elif tool == "summarizer":

        text = input("Enter paragraph:\n")

        print(summarize(text))

    elif tool == "calculator":

        a = float(input("First Number: "))
        b = float(input("Second Number: "))

        op = input("Operation (+,-,*,/): ")

        if op == "+":
            print(add(a,b))

        elif op == "-":
            print(subtract(a,b))

        elif op == "*":
            print(multiply(a,b))

        elif op == "/":
            print(divide(a,b))

        else:
            print("Invalid Operation")

    else:

        print("I don't know which tool to use.")