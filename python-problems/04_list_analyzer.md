# Problem 4: List Analyzer

**Difficulty:** ⭐⭐⭐ Medium

## Problem Description

Write a program that:
1. Takes a list of numbers from the user (comma-separated)
2. Finds and displays:
   - The largest number
   - The smallest number
   - The average (sum / count)
   - How many numbers are even
   - How many numbers are odd

## Learning Goals
- Work with lists
- Loop through lists and analyze data
- Use built-in functions like `max()`, `min()`, `sum()`
- Practice mathematical operations

## Hints to Get Started
1. Ask user to enter numbers separated by commas
2. Split the input using `.split(',')`
3. Convert each string to a number using `int()` or `float()`
4. Use `max()` and `min()` functions to find largest and smallest
5. Use `sum()` to calculate total, then divide by `len()` for average
6. Loop through the list and check if each number is even or odd using `% 2`

## Example

**Input:**
```
Enter numbers separated by commas: 10, 25, 15, 30, 5
```

**Expected Output:**
```
Largest number: 30
Smallest number: 5
Average: 17.0
Even numbers: 3
Odd numbers: 2
```

**Another Example:**
```
Enter numbers separated by commas: 2, 4, 6, 8
```

**Expected Output:**
```
Largest number: 8
Smallest number: 2
Average: 5.0
Even numbers: 4
Odd numbers: 0
```

## Tips
- Use `input().split(',')` to get a list of strings
- Convert to numbers: `[int(x.strip()) for x in numbers]` (or use a loop)
- A number is even if `number % 2 == 0`
- A number is odd if `number % 2 == 1`
- `.strip()` removes extra spaces

## Challenge (Optional)
Calculate the median (middle value when sorted) of the numbers. What happens if there are an even number of values?
