# Problem 1: Simple Calculator

**Difficulty:** ⭐ Easy

## Problem Description

Write a Python program that takes two numbers and an operation (+, -, *, /) as input from the user, then displays the result.

## Learning Goals
- Practice using `input()` function
- Convert strings to numbers using `int()` or `float()`
- Understand basic arithmetic operations in Python

## Hints to Get Started
1. Ask the user to enter the first number using `input()`
2. Ask the user to enter the second number
3. Ask the user to choose an operation
4. Use `if` statements to check which operation was chosen
5. Calculate and print the result

## Example

**Input:**
```
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +
```

**Expected Output:**
```
10 + 5 = 15
```

**Another Example:**
```
Enter first number: 20
Enter second number: 4
Enter operation (+, -, *, /): /
```

**Expected Output:**
```
20 / 4 = 5.0
```

## Tips
- Use `input()` to get user input
- Use `float()` to convert input to decimal numbers
- Be careful with division - what if someone enters 0 as the second number?

## Challenge (Optional)
Add error handling: What happens if the user divides by zero? Make your program handle this gracefully!
