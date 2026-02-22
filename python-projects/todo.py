"""
Simple Command-Line To-Do List Application.

This program allows users to:
- Add tasks
- View tasks
- Remove tasks
- Mark tasks as completed
"""

todo_list = []


def add_task():
    """Add a new task to the to-do list."""
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "Pending"})
    print("New task added successfully!\n")


def view_task():
    """Display all tasks in the to-do list."""
    print("\nYour To-Do List:")
    if len(todo_list) == 0:
        print("No tasks available!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task['Task']} - {task['Status']}")
    print()


def remove_task():
    """Remove a task from the to-do list using task number."""
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("Enter task number to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed: {removed_task['Task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def mark_done():
    """Mark a selected task as completed."""
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]["Status"] = "Done"
                print(f"Task '{todo_list[search_index]['Task']}' marked as Done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def menu():
    """Display the main menu and handle user choices."""
    while True:
        print("***** Main Menu *****")
        print("1. Add a new Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Try again!\n")


if __name__ == "__main__":
    menu()
