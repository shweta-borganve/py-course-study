# Problem 6: Function - Temperature Converter

**Difficulty:** ⭐⭐⭐ Medium

## Problem Description

Write a program with **functions** to convert temperatures between:
- Celsius to Fahrenheit: F = (C × 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) × 5/9
- Celsius to Kelvin: K = C + 273.15

The program should:
1. Ask user which conversion they want
2. Ask for the temperature value
3. Call the appropriate function
4. Display the result

## Learning Goals
- Create and use functions
- Return values from functions
- Organize code into reusable pieces
- Practice function parameters

## Hints to Get Started
1. Create a function `celsius_to_fahrenheit(celsius)` that takes celsius and returns fahrenheit
2. Create a function `fahrenheit_to_celsius(fahrenheit)` that takes fahrenheit and returns celsius
3. Create a function `celsius_to_kelvin(celsius)` that takes celsius and returns kelvin
4. In main code, ask user which conversion they want
5. Get the temperature value from user
6. Call the appropriate function
7. Print the result

## Example

**Input:**
```
Which conversion?
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
Choose (1-3): 1
Enter temperature in Celsius: 0
```

**Expected Output:**
```
0°C = 32.0°F
```

**Another Example:**
```
Which conversion?
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
Choose (1-3): 3
Enter temperature in Celsius: 25
```

**Expected Output:**
```
25°C = 298.15 K
```

## Tips
- Define functions at the top with `def function_name(parameter):`
- Use `return` to send the result back
- Call functions with `function_name(value)`
- Use f-strings for nice output: `f"{celsius}°C = {result}°F"`

## Challenge (Optional)
Add error handling: What if the user enters invalid input? What if they enter a temperature below absolute zero (-273.15°C)?
