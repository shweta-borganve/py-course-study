# Problem 3: Number Pattern Generator

**Difficulty:** ⭐⭐ Easy-Medium

## Problem Description

Write a program that takes a number as input and prints different number patterns. Ask the user which pattern they want:

**Pattern 1:** Print numbers from 1 to N
**Pattern 2:** Print numbers from N to 1 (reverse)
**Pattern 3:** Print multiplication table of N

## Learning Goals
- Practice `for` and `while` loops
- Understand how to control loop iterations
- Practice string formatting with loops

## Hints to Get Started
1. Ask the user to enter a number N
2. Ask which pattern they want (1, 2, or 3)
3. Use a `for` loop to iterate from 1 to N (or N to 1)
4. Print each number with proper formatting

## Example

**Input:**
```
Enter a number: 5
Which pattern? (1=ascending, 2=descending, 3=table): 1
```

**Expected Output:**
```
1 2 3 4 5
```

**Another Example:**
```
Enter a number: 4
Which pattern? (1=ascending, 2=descending, 3=table): 3
```

**Expected Output:**
```
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 28
4 x 9 = 36
4 x 10 = 40
```

## Tips
- Use `range(1, n+1)` to generate numbers from 1 to N
- Use `range(n, 0, -1)` to generate numbers from N down to 1
- Use `print()` with `end=' '` to print on the same line

## Challenge (Optional)
Add Pattern 4: Print a pyramid of numbers like:
```
1
1 2
1 2 3
1 2 3 4
```
