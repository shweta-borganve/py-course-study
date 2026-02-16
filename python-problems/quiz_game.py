"""
quiz_gamer.py

A simple Python Quiz Game that:
- Allows users to take a quiz
- Calculates score and percentage
- Saves quiz history to a file
- Displays previous quiz attempts
"""

import datetime


# ---------------- QUESTIONS DATA ---------------- #

questions = [
    {
        "question": "1. What is Python?",
        "options": [
            "A programming language",
            "A snake",
            "A company",
            "An operating system",
        ],
        "correct": 0,
    },
    {
        "question": "2. Which keyword is used to define a function?",
        "options": ["func", "define", "def", "function"],
        "correct": 2,
    },
    {
        "question": "3. Which data type is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "correct": 3,
    },
    {
        "question": "4. Which operator checks equality?",
        "options": ["=", "==", "!=", ">="],
        "correct": 1,
    },
]


# ---------------- FUNCTION TO ASK QUESTION ---------------- #


def ask_question(q):
    """
    Displays a question and its options.
    Takes validated user input.
    Returns True if correct, otherwise False.
    """
    print("\n" + q["question"])

    for i, option in enumerate(q["options"]):
        print(f"{i + 1}. {option}")

    while True:
        answer = input("Enter option number: ")

        if not answer.isdigit():
            print("Please enter a number.")
            continue

        answer = int(answer) - 1

        if 0 <= answer < len(q["options"]):
            break

        print("Invalid option. Try again.")

    if answer == q["correct"]:
        print("Correct")
        return True

    print("Incorrect")
    correct_answer = q["options"][q["correct"]]
    print("Correct answer is:", correct_answer)
    return False


# ---------------- CALCULATE SCORE ---------------- #


def calculate_score(correct, total):
    """
    Calculates and returns percentage score.
    """
    return (correct / total) * 100


# ---------------- SAVE SCORE ---------------- #


def save_score(name, score, percentage):
    """
    Saves quiz result with timestamp to a text file.
    """
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("quiz_history.txt", "a", encoding="utf-8") as file:
        file.write(f"{time} | {name} | Score: {score} | {percentage:.2f}%\n")


# ---------------- SHOW HISTORY ---------------- #


def show_history():
    """
    Displays previous quiz attempts from file.
    """
    try:
        with open("quiz_history.txt", "r", encoding="utf-8") as file:
            print("\n---- Quiz History ----")
            print(file.read())
    except FileNotFoundError:
        print("\nNo history found yet.")


# ---------------- MAIN PROGRAM ---------------- #


def main():
    """
    Main function to run the quiz game menu system.
    """
    print("===== PYTHON QUIZ GAME =====")

    while True:
        print("\n1. Take Quiz")
        print("2. View Score History")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("\nEnter your name: ")
            correct_answers = 0

            for q in questions:
                if ask_question(q):
                    correct_answers += 1

            total_questions = len(questions)
            percentage = calculate_score(correct_answers, total_questions)

            print("\n===== QUIZ RESULT =====")
            print("Name:", name)
            print("Score:", correct_answers, "/", total_questions)
            print(f"Percentage: {percentage:.2f}%")

            save_score(name, correct_answers, percentage)

            retry = input("\nDo you want to retake the quiz? (yes/no): ")
            if retry.lower() == "yes":
                continue

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Try again.")


# ---------------- RUN PROGRAM ---------------- #

if __name__ == "__main__":
    main()
