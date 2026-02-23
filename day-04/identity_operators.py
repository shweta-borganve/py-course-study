"""
Demonstration of Identity Operators in Python.

This program shows the use of:
- is
- is not
- ==

It explains the difference between identity and equality.
"""


def main():
    """Main function to demonstrate identity operators."""

    # Example 1: Same object reference
    list_a = [1, 2, 3]
    list_b = list_a
    print(list_a is list_b)

    # Example 2: Different objects with same values
    list_c = [1, 2]
    list_d = [1, 2]
    print(list_c == list_d)
    print(list_c is list_d)

    # Example 3: String identity
    string_x = "hello"
    string_y = "world"
    print(string_x is not string_y)

    # Example 4: Checking None
    value = None
    print(value is None)


if __name__ == "__main__":
    main()
