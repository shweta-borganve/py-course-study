# Student Grade Management Program

# Dictionary to store student name and grade
grades = {}

while True:
    print("\n------ Student Grade Management ------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Find Average Grade")
    print("4. Find Highest Grade")
    print("5. Find Lowest Grade")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1️ Add Student
    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        grades[name] = grade
        print("Student added successfully!")

    # 2️ View All Students
    elif choice == "2":
        if len(grades) == 0:
            print("No students available.")
        else:
            print("\nStudent Grades:")
            for name, grade in grades.items():
                print(name, ":", grade)

    # 3️ Average Grade
    elif choice == "3":
        if len(grades) == 0:
            print("No students available.")
        else:
            average = sum(grades.values()) / len(grades)
            print("Average Grade is:", average)

    # 4️ Highest Grade
    elif choice == "4":
        if len(grades) == 0:
            print("No students available.")
        else:
            highest = max(grades.values())
            for name, grade in grades.items():
                if grade == highest:
                    print("Highest Grade is", highest, "by", name)

    # 5️ Lowest Grade
    elif choice == "5":
        if len(grades) == 0:
            print("No students available.")
        else:
            lowest = min(grades.values())
            for name, grade in grades.items():
                if grade == lowest:
                    print("Lowest Grade is", lowest, "by", name)

    # 6️ Exit
    elif choice == "6":
        print("Exiting Program... Thank You!")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")
