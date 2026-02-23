# Problem 9: File Operations - Student Record System

**Difficulty:** ⭐⭐⭐⭐ Medium-Hard

## Problem Description

Create a student record system that **saves data to a file**. The program should:

1. **Create/Read** a file called `students.txt`
2. **Add** new student records to the file (format: `name,age,grade`)
3. **Search** for a student by name
4. **Update** a student's grade
5. **Delete** a student record
6. **Display** all students from the file
7. All changes should be **saved to the file**

## Learning Goals
- Read from files using `open()` and `.readlines()`
- Write to files
- Parse file data (splitting by commas)
- Modify file contents
- Persistent data storage

## Hints to Get Started
1. Open file: `with open('students.txt', 'r') as file:`
2. Read all lines: `lines = file.readlines()`
3. Process each line: `name, age, grade = line.strip().split(',')`
4. Write to file: `with open('students.txt', 'w') as file: file.write(...)`
5. To update: read all, modify in memory, write all back
6. To delete: read all, skip the one to delete, write back

## Example

**Adding a student:**
```
Input: Add new student
Enter name: Alice
Enter age: 20
Enter grade: A
Output: Student added successfully!
```

**File content after adding:**
```
Alice,20,A
Bob,19,B
Carol,21,A
```

**Searching for a student:**
```
Input: Search for Alice
Output:
Found: Alice, Age: 20, Grade: A
```

**Updating a grade:**
```
Input: Update Bob's grade
Enter new grade: A+
Output: Grade updated!
```

**File after update:**
```
Alice,20,A
Bob,19,A+
Carol,21,A
```

**Deleting a student:**
```
Input: Delete Carol
Output: Student deleted!
```

**File after delete:**
```
Alice,20,A
Bob,19,A+
```

## Tips
- Use `with open() as file:` - this automatically closes the file
- `line.strip()` removes newline characters (`\n`)
- `.split(',')` splits by comma
- To write multiple lines: write `name,age,grade\n` (include newline)
- Always validate that a student exists before updating/deleting

## Challenge (Optional)
1. Create a backup of the file before modifying
2. Add sorting - display students sorted by name or grade
3. Add validation - ensure age is a valid number, grade is valid
4. Store the data as JSON instead of CSV for easier parsing
5. Add a statistics feature - average age, count of each grade
