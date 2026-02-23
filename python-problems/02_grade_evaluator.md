# Problem 2: Grade Evaluator

**Difficulty:** ⭐⭐ Easy-Medium

## Problem Description

Write a program that asks a student for their test score (0-100) and displays their grade based on these rules:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

Also display if they passed (60+) or failed (below 60).

## Learning Goals
- Practice using `if-elif-else` statements
- Work with conditional logic
- Handle multiple conditions

## Hints to Get Started
1. Ask the user to input their score
2. Convert the input to a number
3. Check which range the score falls into (use `if-elif-else`)
4. Print the corresponding grade
5. Check if they passed or failed

## Example

**Input:**
```
Enter your test score: 85
```

**Expected Output:**
```
Your grade: B
Status: PASSED
```

**Another Example:**
```
Enter your test score: 55
```

**Expected Output:**
```
Your grade: F
Status: FAILED
```

## Tips
- Use `if score >= 90` for the first condition
- Remember: `elif` (else if) is useful for checking multiple ranges
- The order of conditions matters!

## Challenge (Optional)
Add a feature that calculates the average of 3 test scores and then assigns a final grade based on the average.
