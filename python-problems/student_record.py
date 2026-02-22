"""
Student Record System

This program allows users to:
- Add student records
- Display all students
- Search for a student
- Update student grade
- Delete a student

Records are stored in a text file.
"""

import os

FILENAME = "students.txt"


# Create file if it does not exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8"):
        pass


def add_student():
    """Add a new student record to the file."""
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{name},{age},{grade}\n")

    print("Student added successfully!\n")


def display_students():
    """Display all student records."""
    with open(FILENAME, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("No records found.\n")
        return

    print("\nStudent Records:")
    for line in lines:
        name, age, grade = line.strip().split(",")
        print(f"Name: {name}, Age: {age}, Grade: {grade}")
    print()


def search_student():
    """Search for a student by name."""
    search_name = input("Enter name to search: ")
    found = False

    with open(FILENAME, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        name, age, grade = line.strip().split(",")
        if name.lower() == search_name.lower():
            print(f"Found -> Name: {name}, Age: {age}, Grade: {grade}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")


def update_student():
    """Update a student's grade."""
    update_name = input("Enter name to update: ")
    new_grade = input("Enter new grade: ")
    updated = False

    with open(FILENAME, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(FILENAME, "w", encoding="utf-8") as file:
        for line in lines:
            name, age, _ = line.strip().split(",")
            if name.lower() == update_name.lower():
                file.write(f"{name},{age},{new_grade}\n")
                updated = True
            else:
                file.write(line)

    if updated:
        print("Student grade updated successfully!\n")
    else:
        print("Student not found.\n")


def delete_student():
    """Delete a student record by name."""
    delete_name = input("Enter name to delete: ")
    deleted = False

    with open(FILENAME, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(FILENAME, "w", encoding="utf-8") as file:
        for line in lines:
            name, _, _ = line.strip().split(",")
            if name.lower() != delete_name.lower():
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


def main():
    """Main menu loop for the student record system."""
    while True:
        print("===== Student Record System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student Grade")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
