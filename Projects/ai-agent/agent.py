# Day 11 - Task 4
# Rule-Based AI Agent

import random
from datetime import datetime


# -----------------------------
# Calculator Tool
# -----------------------------
def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation."


# -----------------------------
# Date & Time Tool
# -----------------------------
def current_time():
    now = datetime.now()
    return f"Current Date: {now.strftime('%d-%m-%Y')}\nCurrent Time: {now.strftime('%H:%M:%S')}"


# -----------------------------
# Quote Tool
# -----------------------------
def random_quote():

    quotes = [
        "Believe in yourself.",
        "Never stop learning.",
        "Success comes from consistency.",
        "Dream big and work hard.",
        "Every day is a new opportunity."
    ]

    return random.choice(quotes)


# -----------------------------
# Weather Tool (Mock)
# -----------------------------
def weather(city):

    weather_data = {
        "chennai": "31°C, Sunny",
        "bangalore": "26°C, Cloudy",
        "hyderabad": "30°C, Clear Sky",
        "delhi": "35°C, Hot",
        "mumbai": "29°C, Rainy"
    }

    return weather_data.get(city.lower(), "Weather information not available.")


# -----------------------------
# AI Agent
# -----------------------------
print("===== AI Assistant =====")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        print("AI Agent: Goodbye!")
        break

    elif "time" in user.lower() or "date" in user.lower():
        print("\nAI Agent:")
        print(current_time())

    elif "motivation" in user.lower() or "quote" in user.lower():
        print("\nAI Agent:")
        print(random_quote())

    elif "weather" in user.lower():

        city = input("Enter city: ")

        print("\nAI Agent:")
        print(weather(city))

    elif any(op in user for op in ["+", "-", "*", "/"]):

        print("\nAI Agent:")
        print(calculate(user))

    else:

        print("\nAI Agent:")
        print("Sorry, I don't know which tool to use for that request.")