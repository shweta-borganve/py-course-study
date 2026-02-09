# Problem 7: Student Grade Manager

**Difficulty:** ⭐⭐⭐⭐ Medium-Hard

## Problem Description

Create a program to manage student grades using a **dictionary**. The program should:
1. Allow adding students with their grades (as a dictionary)
2. Calculate the average grade for all students
3. Find the student with the highest grade
4. Find the student with the lowest grade
5. Display all students and their grades

The program should keep running in a loop until the user chooses to exit.

## Learning Goals
- Work with dictionaries
- Dictionary methods (`.values()`, `.keys()`, `.items()`)
- Loops and menu-driven programming
- Data management

## Hints to Get Started
1. Create a dictionary to store student_name: grade pairs
2. Use a `while` loop to keep the program running
3. Show a menu: Add student, View all, Find highest, Find lowest, Average, Exit
4. Use `if-elif` to handle menu choices
5. For average: use `sum(grades.values()) / len(grades)`
6. For highest: use `max(grades.values())` and find which student has it
7. For lowest: use `min(grades.values())`

## Example

**Input/Output Flow:**
```
=== Student Grade Manager ===
1. Add student
2. View all students
3. Find highest grade
4. Find lowest grade
5. Calculate average
6. Exit
Choose an option: 1
Enter student name: Alice
Enter grade: 85
Student added!

Choose an option: 1
Enter student name: Bob
Enter grade: 92
Student added!

Choose an option: 2
```

**Expected Output for "View all":**
```
Student Grades:
Alice: 85
Bob: 92
```

**Expected Output for "Highest":**
```
Highest grade: Bob with 92
```

**Expected Output for "Average":**
```
Average grade: 88.5
```

## Tips
- Create dictionary: `students = {}`
- Add to dictionary: `students[name] = grade`
- Loop through dictionary: `for name, grade in students.items():`
- Use `if name not in students:` to check if student exists
- Use `while True:` for infinite loop, `break` to exit

## Challenge (Optional)
Add a feature to:
- Remove a student
- Update a student's grade
- Show grades in descending order
- Calculate letter grades (A, B, C, D, F) for each student
