"""
This module demonstrates the use of membership operators in Python.
"""


def check_membership():
    """Check membership in different data types."""

    numbers = [10, 20, 30, 40]
    print(20 in numbers)

    text_value = "python"
    print("py" in text_value)

    data = (1, 2, 3, 4)
    print(3 in data)


if __name__ == "__main__":
    check_membership()

# Check membership operators in Python

numbers = [10, 20, 30, 40]
print(20 in numbers)

text = "python"
print("py" in text)

data = (1, 2, 3, 4)
print(3 in data)

