# Day 11 - Task 3
# Simple Python Tools

import random
from datetime import datetime

# -----------------------------
# Tool 1: Calculator
# -----------------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# -----------------------------
# Tool 2: Current Date & Time
# -----------------------------
def current_datetime():
    now = datetime.now()

    print("Current Date :", now.strftime("%d-%m-%Y"))
    print("Current Time :", now.strftime("%H:%M:%S"))


# -----------------------------
# Tool 3: Random Quote Generator
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
# Tool 4: Mock Weather Lookup
# -----------------------------
def weather(city):

    weather_data = {
        "Chennai": "31°C, Sunny",
        "Bangalore": "26°C, Cloudy",
        "Hyderabad": "30°C, Clear Sky",
        "Delhi": "35°C, Hot",
        "Mumbai": "29°C, Rainy"
    }

    return weather_data.get(city, "Weather data not available.")


# -----------------------------
# Demo
# -----------------------------
print("===== Calculator =====")
print("10 + 5 =", add(10, 5))
print("10 - 5 =", subtract(10, 5))
print("10 * 5 =", multiply(10, 5))
print("10 / 5 =", divide(10, 5))

print("\n===== Date & Time =====")
current_datetime()

print("\n===== Random Quote =====")
print(random_quote())

print("\n===== Weather =====")
print(weather("Chennai"))