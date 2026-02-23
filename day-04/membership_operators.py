"""
This module demonstrates the use of membership operators in Python.
"""


def check_membership():
    """Check membership in different data types."""

    num_list = [10, 20, 30, 40]
    print(20 in num_list)

    text_value = "python"
    print("py" in text_value)

    data_tuple = (1, 2, 3, 4)
    print(3 in data_tuple)


if __name__ == "__main__":
    check_membership()

# Global examples of membership operators

NUMBERS = [10, 20, 30, 40]
print(20 in NUMBERS)

TEXT = "python"
print("py" in TEXT)

DATA = (1, 2, 3, 4)
print(3 in DATA)
