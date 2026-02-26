"""
This module demonstrates different ways to update strings in Python.
"""


def demonstrate_string_updates():
    """Show examples of string modification techniques."""

    msg = "Hello"
    msg = msg + " World"
    print(msg)

    text = "I like Java"
    text = text.replace("Java", "Python")
    print(text)

    word = "Python"
    new_word = word[:3] + "XYZ"
    print(new_word)

    text = "hello"
    text = text.upper()
    print(text)


if __name__ == "__main__":
    demonstrate_string_updates()
