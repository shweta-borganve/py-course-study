import os

FILENAME = "students.txt"

# Create file if it does not exist
if not os.path.exists(FILENAME):
    open(FILENAME, "w").close()


# Add Student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    with open(FILENAME, "a") as file:
        file.write(f"{name},{age},{grade}\n")

    print("Student added successfully!\n")


# Display All Students
def display_students():
    with open(FILENAME, "r") as file:
        lines = file.readlines()

    if not lines:
        print("No records found.\n")
        return

    print("\nStudent Records:")
    for line in lines:
        name, age, grade = line.strip().split(",")
        print(f"Name: {name}, Age: {age}, Grade: {grade}")
    print()


# Search Student
def search_student():
    search_name = input("Enter name to search: ")
    found = False

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    for line in lines:
        name, age, grade = line.strip().split(",")
        if name.lower() == search_name.lower():
            print(f"Found -> Name: {name}, Age: {age}, Grade: {grade}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")


# Update Student Grade
def update_student():
    update_name = input("Enter name to update: ")
    new_grade = input("Enter new grade: ")
    updated = False

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    with open(FILENAME, "w") as file:
        for line in lines:
            name, age, grade = line.strip().split(",")
            if name.lower() == update_name.lower():
                file.write(f"{name},{age},{new_grade}\n")
                updated = True
            else:
                file.write(line)

    if updated:
        print("Student grade updated successfully!\n")
    else:
        print("Student not found.\n")


# Delete Student
def delete_student():
    delete_name = input("Enter name to delete: ")
    deleted = False

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    with open(FILENAME, "w") as file:
        for line in lines:
            name, age, grade = line.strip().split(",")
            if name.lower() != delete_name.lower():
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


# Main Menu Loop
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
