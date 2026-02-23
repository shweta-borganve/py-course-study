"""
Program to demonstrate logical operators in Python.
"""


def demonstrate_logical_operators():
    """Demonstrates AND, OR, and NOT logical operators."""

    # AND operator
    a_value = 10
    b_value = 20
    print(a_value > 5 and b_value > 15)

    # OR operator
    a_value = 10
    b_value = 20
    print(a_value > 50 or b_value > 15)

    # NOT operator
    a_value = 10
    print(a_value <= 5)

    # Real-world example
    age = 22
    has_id = True
    print(age >= 18 and has_id)


if __name__ == "__main__":
    demonstrate_logical_operators()
