# Project 1: To-Do List Manager

**Difficulty:** ⭐⭐ Easy-Medium  
**Real-world Use:** Task management for personal productivity

## Project Overview

Build a command-line **To-Do List Manager** where users can:
- Add tasks with priority (High, Medium, Low)
- Mark tasks as complete
- View all tasks (with filtering options)
- Delete tasks
- Save tasks to a file so they persist between sessions

## Features to Implement

1. **Add Task**: User enters task description and priority
   - Tasks should have: ID, description, priority, completion status, creation date

2. **View Tasks**: 
   - Show all tasks
   - Show only pending tasks
   - Show only completed tasks
   - Sort by priority (High → Medium → Low)

3. **Mark Complete**: User marks a task as done
   - Show completion date/time

4. **Delete Task**: Remove a task by ID

5. **Data Persistence**:
   - Save to `tasks.txt` or JSON file
   - Load tasks when program starts
   - Auto-save after each change

6. **Statistics**:
   - Show total tasks
   - Show completed count
   - Show pending count
   - Show completion percentage

## Technologies/Concepts Needed
- File I/O (read/write)
- Data structures (lists, dictionaries)
- Loops and conditionals
- String manipulation
- Date/time handling
- JSON (optional, for better data format)

## Step-by-Step Guidance

### Step 1: Design Data Structure
```python
tasks = [
    {
        "id": 1,
        "description": "Complete Python project",
        "priority": "High",
        "completed": False,
        "created_date": "2025-02-09"
    }
]
```

### Step 2: Create Core Functions
- `add_task(description, priority)`
- `view_tasks(filter_type='all')`
- `mark_complete(task_id)`
- `delete_task(task_id)`
- `save_tasks()`
- `load_tasks()`

### Step 3: Build Menu System
```
=== To-Do List Manager ===
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Mark Task Complete
6. Delete Task
7. Show Statistics
8. Exit
```

### Step 4: Implement File Operations
- Load tasks from file on startup
- Save after each modification

## Example Usage

```
=== To-Do List Manager ===
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Mark Task Complete
6. Delete Task
7. Show Statistics
8. Exit

Choose option: 1
Enter task description: Complete Python assignment
Enter priority (High/Medium/Low): High
✓ Task added successfully! (ID: 1)

Choose option: 2
All Tasks:
[1] Complete Python assignment (High) - PENDING - Created: 2025-02-09

Choose option: 7
=== Statistics ===
Total Tasks: 1
Completed: 0
Pending: 1
Completion Rate: 0%
```

## Real-World Enhancement Ideas
1. **Categories**: Organize tasks by categories (Work, Personal, School)
2. **Due Dates**: Add deadline tracking and reminders
3. **Recurring Tasks**: Daily, weekly, monthly tasks
4. **Task Notes**: Add detailed descriptions
5. **Export**: Export to CSV for backup
6. **Search**: Find tasks by keyword
7. **Time Tracking**: Track how long tasks take

## Grading Criteria
- ✅ Can add, view, delete tasks
- ✅ Priority system works correctly
- ✅ Data persists between sessions
- ✅ Menu system is user-friendly
- ✅ Statistics are accurate
- ✅ Code is well-organized with functions
