"""
This module implements a simple calculator program.
It performs addition, subtraction, multiplication,
and division based on user input.
"""


def main():
    """Run the simple calculator program."""

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result =", num1 + num2)

    elif op == "-":
        print("Result =", num1 - num2)

    elif op == "*":
        print("Result =", num1 * num2)

    elif op == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid operation")


if __name__ == "__main__":
    main()
