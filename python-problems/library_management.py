"""
Library Management System

This module allows users to:
- Search books by title, author, or category
- Checkout and return books
- View unavailable books
- Add new books
"""

import datetime


LIBRARY = {
    "Programming": [
        {
            "title": "Python Basics",
            "author": "John Smith",
            "copies": 3,
            "borrowers": [],
        },
        {
            "title": "C Programming",
            "author": "Dennis Ritchie",
            "copies": 2,
            "borrowers": [],
        },
    ],
    "Fiction": [
        {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "copies": 1,
            "borrowers": [],
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "copies": 0,
            "borrowers": [],
        },
    ],
    "Science": [
        {
            "title": "Physics Fundamentals",
            "author": "Isaac Newton",
            "copies": 4,
            "borrowers": [],
        }
    ],
}


def search_by_title(book_title):
    """Search for a book by its title."""
    for category_name, books in LIBRARY.items():
        for book in books:
            if book["title"].lower() == book_title.lower():
                print("Book Found:")
                print("Category:", category_name)
                print("Author:", book["author"])
                print("Available Copies:", book["copies"])
                return
    print("Book not found.")


def search_by_author(author_name):
    """Search for books by a specific author."""
    found = False
    for category_name, books in LIBRARY.items():
        for book in books:
            if book["author"].lower() == author_name.lower():
                print("Title:", book["title"])
                print("Category:", category_name)
                print("Copies:", book["copies"])
                print("-" * 30)
                found = True

    if not found:
        print("No books found by this author.")


def search_by_category(category_name):
    """Display all books in a given category."""
    if category_name in LIBRARY:
        print("Books in", category_name)
        for book in LIBRARY[category_name]:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Copies:", book["copies"])
            print("-" * 30)
    else:
        print("Category not found.")


def checkout_book(book_title, user_name):
    """Checkout a book for a user."""
    for books in LIBRARY.values():
        for book in books:
            if book["title"].lower() == book_title.lower():
                if book["copies"] <= 0:
                    print("No copies available.")
                    return

                book["copies"] -= 1
                today = datetime.date.today()
                due_date = today + datetime.timedelta(days=7)

                borrower_data = {
                    "user": user_name,
                    "due_date": due_date,
                }

                book["borrowers"].append(borrower_data)

                print("Book checked out successfully.")
                print("Due Date:", due_date)
                return

    print("Book not found.")


def return_book(book_title, user_name):
    """Return a borrowed book."""
    for books in LIBRARY.values():
        for book in books:
            if book["title"].lower() != book_title.lower():
                continue

            borrower_record = next(
                (b for b in book["borrowers"] if b["user"] == user_name),
                None,
            )

            if borrower_record is None:
                print("User did not borrow this book.")
                return

            book["copies"] += 1
            today = datetime.date.today()
            due_date = borrower_record["due_date"]

            if today > due_date:
                late_days = (today - due_date).days
                fine = late_days * 5
                print("Returned late.")
                print("Fine:", fine, "rupees")
            else:
                print("Returned on time.")
                print("No fine.")

            book["borrowers"].remove(borrower_record)
            return

    print("Book not found.")


def show_books_in_category(category_name):
    """Show books in a specific category."""
    search_by_category(category_name)


def show_unavailable_books():
    """Display books that have zero copies available."""
    print("Books with No Copies Available:")
    found = False

    for category_name, books in LIBRARY.items():
        for book in books:
            if book["copies"] == 0:
                print("Title:", book["title"])
                print("Category:", category_name)
                print("-" * 30)
                found = True

    if not found:
        print("All books are available.")


def add_book(category_name, book_title, author_name, number_of_copies):
    """Add a new book to the library."""
    if category_name not in LIBRARY:
        LIBRARY[category_name] = []

    new_book = {
        "title": book_title,
        "author": author_name,
        "copies": number_of_copies,
        "borrowers": [],
    }

    LIBRARY[category_name].append(new_book)
    print("Book added successfully.")


def main():
    """Main menu loop for the library system."""
    while True:
        print("\n----- Library Menu -----")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Search by Category")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Show Books in Category")
        print("7. Show Unavailable Books")
        print("8. Add Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_by_title(input("Enter title: "))

        elif choice == "2":
            search_by_author(input("Enter author: "))

        elif choice == "3":
            search_by_category(input("Enter category: "))

        elif choice == "4":
            checkout_book(
                input("Enter title: "),
                input("Enter your name: "),
            )

        elif choice == "5":
            return_book(
                input("Enter title: "),
                input("Enter your name: "),
            )

        elif choice == "6":
            show_books_in_category(input("Enter category: "))

        elif choice == "7":
            show_unavailable_books()

        elif choice == "8":
            add_book(
                input("Enter category: "),
                input("Enter title: "),
                input("Enter author: "),
                int(input("Enter number of copies: ")),
            )

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
