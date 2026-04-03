"""Pylint 10/10 Chatbot Implementation."""

import json
import os
import random
import re
from datetime import datetime


class Chatbot:
    """A simple rule-based chatbot with memory."""

    def __init__(self, name="PyBot", memory_file="bot_memory.json"):
        """Initialize chatbot."""
        self.name = name
        self.memory_file = memory_file
        self.user_info = {}
        self.todos = []

        self.responses = {
            "greet": ("Hello!", "Hi there!", "Hey!"),
            "bye": ("Goodbye!", "See you!", "Take care!"),
            "unknown": (
                "I didn't understand that.",
                "Could you rephrase?",
                "Try asking something else.",
            ),
        }

        self._load_data()

    # ---------------- FILE HANDLING ---------------- #
    def _load_data(self):
        """Load stored data from file."""
        if not os.path.exists(self.memory_file):
            return

        try:
            with open(self.memory_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Memory file corrupted. Starting fresh.")
            return

        self.user_info = data.get("user_info", {})
        self.todos = data.get("todos", [])

    def _save_data(self):
        """Save data to file."""
        data = {
            "user_info": self.user_info,
            "todos": self.todos,
        }

        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    # ---------------- UTILITIES ---------------- #
    def _random_response(self, key):
        """Return random response."""
        return random.choice(self.responses.get(key, ("...",)))

    def _safe_calculate(self, text):
        """Perform safe arithmetic calculation."""
        response = "Invalid expression."
        match = re.search(r"(\d+)\s*([+\-*/])\s*(\d+)", text)

        if match:
            num1, operator, num2 = match.groups()
            num1_int = int(num1)
            num2_int = int(num2)

            if operator == "+":
                response = str(num1_int + num2_int)
            elif operator == "-":
                response = str(num1_int - num2_int)
            elif operator == "*":
                response = str(num1_int * num2_int)
            elif operator == "/":
                if num2_int == 0:
                    response = "Cannot divide by zero."
                else:
                    response = str(num1_int / num2_int)

        return response

    # ---------------- CORE LOGIC ---------------- #
    def handle_input(self, user_input):
        """Process user input and return response."""
        text = user_input.lower().strip()
        response = ""

        if re.search(r"\b(hi|hello|hey)\b", text):
            response = self._random_response("greet")

        elif re.search(r"\b(bye|exit|quit)\b", text):
            response = self._random_response("bye")

        elif re.search(r"\d+\s*[+\-*/]\s*\d+", text):
            response = self._safe_calculate(text)

        elif "my name is" in text:
            name = user_input.split()[-1].capitalize()
            self.user_info["name"] = name
            response = f"Nice to meet you, {name}!"

        elif "what is my name" in text:
            response = self.user_info.get(
                "name", "I don't know your name yet."
            )

        elif "add todo" in text:
            task = user_input.replace("add todo", "").strip()
            self.todos.append(task)
            response = f"Added: {task}"

        elif "show todo" in text:
            if self.todos:
                response = "\n".join(self.todos)
            else:
                response = "Todo list is empty."

        elif "time" in text:
            response = datetime.now().strftime("Time: %I:%M %p")

        elif "date" in text:
            response = datetime.now().strftime("Date: %B %d, %Y")

        else:
            response = self._random_response("unknown")

        return response

    # ---------------- RUN ---------------- #
    def run(self):
        """Run chatbot loop safely."""
        print(f"{self.name} started. Type 'exit' to quit.")

        while True:
            try:
                user_input = input("You: ")
            except OSError:
                print("Input not supported in this environment.")
                break
            except KeyboardInterrupt:
                print("\nExiting chatbot.")
                break

            if user_input.lower() in {"exit", "quit"}:
                print(self._random_response("bye"))
                break

            response = self.handle_input(user_input)
            print(f"{self.name}: {response}")
            self._save_data()


def main():
    """Entry point."""
    chatbot = Chatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
