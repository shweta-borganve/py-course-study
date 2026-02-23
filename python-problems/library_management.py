# Library Management System

import datetime

library = {
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


def search_by_title(title):
    for category, books in library.items():
        for book in books:
            if book["title"].lower() == title.lower():
                print("Book Found:")
                print("Category:", category)
                print("Author:", book["author"])
                print("Available Copies:", book["copies"])
                return

    print("Book not found.")


def search_by_author(author):
    found = False

    for category, books in library.items():
        for book in books:
            if book["author"].lower() == author.lower():
                print("Title:", book["title"])
                print("Category:", category)
                print("Copies:", book["copies"])
                print("-" * 30)
                found = True

    if not found:
        print("No books found by this author.")


def search_by_category(category):
    if category in library:
        print("Books in", category)

        for book in library[category]:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Copies:", book["copies"])
            print("-" * 30)
    else:
        print("Category not found.")


def checkout_book(title, user):
    for books in library.values():
        for book in books:
            if book["title"].lower() == title.lower():

                if book["copies"] > 0:
                    book["copies"] -= 1

                    today = datetime.date.today()
                    due_date = today + datetime.timedelta(days=7)

                    borrower_data = {
                        "user": user,
                        "due_date": due_date,
                    }

                    book["borrowers"].append(borrower_data)

                    print("Book checked out successfully.")
                    print("Due Date:", due_date)
                    return

                print("No copies available.")
                return

    print("Book not found.")


def return_book(title, user):
    for books in library.values():
        for book in books:
            if book["title"].lower() == title.lower():

                for borrower in book["borrowers"]:
                    if borrower["user"] == user:

                        book["copies"] += 1

                        today = datetime.date.today()
                        due_date = borrower["due_date"]

                        if today > due_date:
                            late_days = (today - due_date).days
                            fine = late_days * 5

                            print("Returned late.")
                            print("Fine:", fine, "rupees")
                        else:
                            print("Returned on time.")
                            print("No fine.")

                        book["borrowers"].remove(borrower)
                        return

                print("User did not borrow this book.")
                return

    print("Book not found.")


def show_books_in_category(category):
    search_by_category(category)


def show_unavailable_books():
    print("Books with No Copies Available:")

    found = False

    for category, books in library.items():
        for book in books:
            if book["copies"] == 0:
                print("Title:", book["title"])
                print("Category:", category)
                print("-" * 30)
                found = True

    if not found:
        print("All books are available.")


def add_book(category, title, author, copies):
    if category not in library:
        library[category] = []

    new_book = {
        "title": title,
        "author": author,
        "copies": copies,
        "borrowers": [],
    }

    library[category].append(new_book)

    print("Book added successfully.")


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
        title = input("Enter title: ")
        search_by_title(title)

    elif choice == "2":
        author = input("Enter author: ")
        search_by_author(author)

    elif choice == "3":
        category = input("Enter category: ")
        search_by_category(category)

    elif choice == "4":
        title = input("Enter title: ")
        user = input("Enter your name: ")
        checkout_book(title, user)

    elif choice == "5":
        title = input("Enter title: ")
        user = input("Enter your name: ")
        return_book(title, user)

    elif choice == "6":
        category = input("Enter category: ")
        show_books_in_category(category)

    elif choice == "7":
        show_unavailable_books()

    elif choice == "8":
        category = input("Enter category: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        copies_input = input("Enter number of copies: ")
        copies = int(copies_input)

        add_book(category, title, author, copies)

    elif choice == "9":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
