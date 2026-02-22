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
# ask student score
score = int(input("Enter your test score (0-100): "))

# check grade using conditions
if score >= 90 and score <= 100:
    print("Grade: A")

elif score >= 80 and score <= 89:
    print("Grade: B")

elif score >= 70 and score <= 79:
    print("Grade: C")

elif score >= 60 and score <= 69:
    print("Grade: D")

elif score < 60 and score >= 0:
    print("Grade: F")

else:
    print("Invalid score")
