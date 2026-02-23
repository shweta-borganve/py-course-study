"""
Simple To-Do List Manager

This program allows users to:
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


def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    """Add a new task."""
    description = input("Enter task description: ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority,
        "completed": False,
        "created_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(
            f"{task['id']}. {task['description']} " f"({task['priority']}) - {status}"
        )


def mark_complete(tasks):
    """Mark a task as completed."""
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete!")
            return

    print("Task not found.")


def delete_task(tasks):
    """Delete a task by ID."""
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(updated_tasks)
        tasks.clear()
        tasks.extend(updated_tasks)
        print("Task deleted.")


def show_statistics(tasks):
    """Display task statistics."""
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed

    print("=== Statistics ===")
    print("Total tasks:", total)
    print("Completed:", completed)
    print("Pending:", pending)


def main():
    """Main menu loop."""
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Choose option: ")

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
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
