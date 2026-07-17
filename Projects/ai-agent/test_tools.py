from tools.calculator import *
from tools.datetime_tool import get_datetime
from tools.summarizer import summarize
from tools.random_fact import random_fact

print(add(10,5))
print(subtract(10,5))
print(multiply(10,5))
print(divide(10,5))

dt = get_datetime()

print("Date :", dt["date"])
print("Time :", dt["time"])

text = """
Artificial Intelligence is changing the world.
It is used in healthcare, education and finance.
It improves productivity.
"""

print(summarize(text))

print(random_fact())