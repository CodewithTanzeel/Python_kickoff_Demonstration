# main.py

# Formal comment: Entry point of the Greet Me! project

from greetings import say_hello
from greetings import log_greeting
import argparse

def kickoff():
    """
    This function starts the program and handles CLI arguments.
    """
    parser = argparse.ArgumentParser(description="Greet the user by name.")
    parser.add_argument("name", help="Enter your name")
    args = parser.parse_args()

    message = say_hello(args.name)
    print(message)
    log =log_greeting(args.name)

# Ensures this script only runs when executed directly
if __name__ == "__main__":
    kickoff()
