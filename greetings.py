# greetings.py

# Formal comment: This module contains greeting logic.
from datetime import datetime


def say_hello(name: str) -> str:
    hour = datetime.now().hour
    if hour < 12:
        part_of_day = "Good morning"
    elif hour < 18:
        part_of_day = "Good afternoon"
    else:
        part_of_day = "Good evening"
    return f"{part_of_day}, {name}! Welcome to Kickoff Python."


def log_greeting(message: str):
    with open("greetings.log", "a") as file:
        file.write(message + "\n")
