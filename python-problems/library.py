"""
Library Management System

This program manages books using nested dictionaries and lists.
It supports searching, checkout, return, and adding books.
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


def search_by_title(search_title):
    """Search a book by its title."""
    for cat_name, book_list in LIBRARY.items():
        for book in book_list:
            if book["title"].lower() == search_title.lower():
                print("Book Found:")
                print("Category:", cat_name)
                print("Author:", book["author"])
                print("Copies:", book["copies"])
                return
    print("Book not found.")


def search_by_author(search_author):
    """Search books by author name."""
    found_book = False

    for cat_name, book_list in LIBRARY.items():
        for book in book_list:
            if book["author"].lower() == search_author.lower():
                print("Title:", book["title"])
                print("Category:", cat_name)
                print("Copies:", book["copies"])
                print("-" * 30)
                found_book = True

    if not found_book:
        print("No books found by this author.")


def search_by_category(cat_input):
    """Show books inside a category."""
    if cat_input in LIBRARY:
        for book in LIBRARY[cat_input]:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Copies:", book["copies"])
            print("-" * 30)
    else:
        print("Category not found.")


def checkout_book(book_title, username):
    """Checkout a book for a user."""
    for book_list in LIBRARY.values():
        for book in book_list:
            if book["title"].lower() == book_title.lower():

                if book["copies"] <= 0:
                    print("No copies available.")
                    return

                book["copies"] -= 1

                due_date = datetime.date.today() + datetime.timedelta(days=7)

                book["borrowers"].append({"user": username, "due_date": due_date})

                print("Book checked out.")
                print("Due Date:", due_date)
                return

    print("Book not found.")


def return_book(book_title, username):
    """Return a borrowed book."""
    for book_list in LIBRARY.values():
        for book in book_list:
            if book["title"].lower() != book_title.lower():
                continue

            borrower_record = next(
                (b for b in book["borrowers"] if b["user"] == username), None
            )

            if borrower_record is None:
                print("User did not borrow this book.")
                return

            book["copies"] += 1
            book["borrowers"].remove(borrower_record)

            today = datetime.date.today()
            due_date = borrower_record["due_date"]

            if today > due_date:
                late_days = (today - due_date).days
                fine = late_days * 5
                print("Returned late.")
                print("Fine:", fine)
            else:
                print("Returned on time.")
                print("No fine.")

            return

    print("Book not found.")


def show_unavailable_books():
    """Display books with zero copies."""
    found = False

    for cat_name, book_list in LIBRARY.items():
        for book in book_list:
            if book["copies"] == 0:
                print("Title:", book["title"])
                print("Category:", cat_name)
                print("-" * 30)
                found = True

    if not found:
        print("All books available.")


def add_new_book(cat_name, book_title, book_author, book_copies):
    """Add a new book to the library."""
    if cat_name not in LIBRARY:
        LIBRARY[cat_name] = []

    LIBRARY[cat_name].append(
        {
            "title": book_title,
            "author": book_author,
            "copies": book_copies,
            "borrowers": [],
        }
    )

    print("Book added successfully.")


def main():
    """Main menu loop."""
    while True:
        print("\n----- Library Menu -----")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Search by Category")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Show Unavailable Books")
        print("7. Add Book")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user_title = input("Enter title: ")
            search_by_title(user_title)

        elif choice == "2":
            user_author = input("Enter author: ")
            search_by_author(user_author)

        elif choice == "3":
            user_category = input("Enter category: ")
            search_by_category(user_category)

        elif choice == "4":
            user_title = input("Enter title: ")
            user_name = input("Enter your name: ")
            checkout_book(user_title, user_name)

        elif choice == "5":
            user_title = input("Enter title: ")
            user_name = input("Enter your name: ")
            return_book(user_title, user_name)

        elif choice == "6":
            show_unavailable_books()

        elif choice == "7":
            user_category = input("Enter category: ")
            user_title = input("Enter title: ")
            user_author = input("Enter author: ")
            copies_input = input("Enter number of copies: ")
            user_copies = int(copies_input)

            add_new_book(user_category, user_title, user_author, user_copies)

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
