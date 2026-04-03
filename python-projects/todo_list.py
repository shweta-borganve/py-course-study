"""
Simple To-Do List Manager

Features:
- Add tasks with priority
- View tasks
- Mark tasks as complete
- Delete tasks
- Show statistics
- Save tasks using JSON file
"""

import json
from datetime import datetime

TASKS_FILE = "tasks.json"
VALID_PRIORITIES = {"High", "Medium", "Low"}


def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def generate_id(tasks):
    """Generate unique task ID."""
    return max((task["id"] for task in tasks), default=0) + 1


def add_task(tasks):
    """Add a new task."""
    description = input("Enter task description: ").strip()
    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    if priority not in VALID_PRIORITIES:
        print("Invalid priority. Setting to 'Low'.")
        priority = "Low"

    task = {
        "id": generate_id(tasks),
        "description": description,
        "priority": priority,
        "completed": False,
        "created_date": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        ),
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Task List ---")
    for task in tasks:
        status = "✔ Done" if task["completed"] else "⏳ Pending"
        print(
            f"{task['id']}. {task['description']} "
            f"[{task['priority']}] - {status}"
        )


def mark_complete(tasks):
    """Mark a task as completed."""
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid input.")
        return

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            found = True
            break

    if found:
        save_tasks(tasks)
        print("✅ Task marked as complete!")
    else:
        print("Task not found.")


def delete_task(tasks):
    """Delete a task."""
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid input.")
        return

    initial_length = len(tasks)

    tasks[:] = [
        task for task in tasks if task["id"] != task_id
    ]

    if len(tasks) < initial_length:
        save_tasks(tasks)
        print("🗑 Task deleted.")
    else:
        print("Task not found.")


def show_statistics(tasks):
    """Display task statistics."""
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed

    print("\n=== Statistics ===")
    print(f"Total Tasks : {total}")
    print(f"Completed   : {completed}")
    print(f"Pending     : {pending}")


def main():
    """Main menu."""
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            show_statistics(tasks)
        elif choice == "6":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
