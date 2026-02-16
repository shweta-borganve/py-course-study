"""
Grade Evaluator Program
This program takes a student's test score (0-100)
and prints the corresponding grade.
"""

# Ask student score
score = int(input("Enter your test score (0-100): "))

# Check grade using conditions
if 90 <= score <= 100:
    print("Grade: A")

elif 80 <= score <= 89:
    print("Grade: B")

elif 70 <= score <= 79:
    print("Grade: C")

elif 60 <= score <= 69:
    print("Grade: D")

elif 0 <= score < 60:
    print("Grade: F")

else:
    print("Invalid score")
