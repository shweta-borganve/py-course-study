"""Simple rule-based chatbot with memory support."""

import json
import os
import random
import re
from datetime import datetime
from typing import Dict, List


class Chatbot:
    """A simple rule-based chatbot."""

    def __init__(self, name: str = "PyBot", memory_file: str = "bot_memory.json") -> None:
        """Initialize chatbot."""
        self.name = name
        self.memory_file = memory_file
        self.user_info: Dict[str, str] = {}
        self.todos: List[str] = []

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
    def _load_data(self) -> None:
        """Load stored data."""
        if not os.path.exists(self.memory_file):
            return

        try:
            with open(self.memory_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Memory file issue. Starting fresh.")
            return

        self.user_info = data.get("user_info", {})
        self.todos = data.get("todos", [])

    def _save_data(self) -> None:
        """Save data."""
        data = {
            "user_info": self.user_info,
            "todos": self.todos,
        }

        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    # ---------------- UTILITIES ---------------- #
    def _random_response(self, key: str) -> str:
        """Return random response."""
        return random.choice(self.responses.get(key, ("...",)))

    def _safe_calculate(self, text: str) -> str:
        """Perform safe arithmetic."""
        match = re.search(r"(\d+)\s*([+\-*/])\s*(\d+)", text)
        if not match:
            return "Invalid expression."

        num1, operator, num2 = match.groups()
        num1_int, num2_int = int(num1), int(num2)

        if operator == "+":
            return str(num1_int + num2_int)
        if operator == "-":
            return str(num1_int - num2_int)
        if operator == "*":
            return str(num1_int * num2_int)
        if operator == "/":
            return "Cannot divide by zero." if num2_int == 0 else str(num1_int / num2_int)

        return "Invalid expression."

    # ---------------- FEATURE HANDLERS ---------------- #
    def _handle_name(self, text: str, user_input: str) -> str:
        """Handle name storage and retrieval."""
        if "my name is" in text:
            name = user_input.split()[-1].capitalize()
            self.user_info["name"] = name
            return f"Nice to meet you, {name}!"

        if "what is my name" in text:
            return self.user_info.get("name", "I don't know your name yet.")

        return ""

    def _handle_todo(self, text: str, user_input: str) -> str:
        """Handle todo operations."""
        if "add todo" in text:
            task = user_input.replace("add todo", "").strip()
            self.todos.append(task)
            return f"Added: {task}"

        if "show todo" in text:
            return "\n".join(self.todos) if self.todos else "Todo list is empty."

        return ""

    def _handle_datetime(self, text: str) -> str:
        """Handle date and time."""
        if "time" in text:
            return datetime.now().strftime("Time: %I:%M %p")

        if "date" in text:
            return datetime.now().strftime("Date: %B %d, %Y")

        return ""

    # ---------------- CORE LOGIC ---------------- #
    def handle_input(self, user_input: str) -> str:
        """Process input."""
        text = user_input.lower().strip()

        if re.search(r"\b(hi|hello|hey)\b", text):
            return self._random_response("greet")

        if re.search(r"\b(bye|exit|quit)\b", text):
            return self._random_response("bye")

        if re.search(r"\d+\s*[+\-*/]\s*\d+", text):
            return self._safe_calculate(text)

        for handler in (self._handle_name, self._handle_todo):
            response = handler(text, user_input)
            if response:
                return response

        datetime_response = self._handle_datetime(text)
        if datetime_response:
            return datetime_response

        return self._random_response("unknown")

    # ---------------- RUN ---------------- #
    def run(self) -> None:
        """Run chatbot."""
        print(f"{self.name} started. Type 'exit' to quit.")

        while True:
            try:
                user_input = input("You: ")
            except (OSError, KeyboardInterrupt):
                print("\nExiting chatbot.")
                break

            if user_input.lower() in {"exit", "quit"}:
                print(self._random_response("bye"))
                break

            response = self.handle_input(user_input)
            print(f"{self.name}: {response}")
            self._save_data()


def main() -> None:
    """Program entry point."""
    Chatbot().run()


if __name__ == "__main__":
    main()
