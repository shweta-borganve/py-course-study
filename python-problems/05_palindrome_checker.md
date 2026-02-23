# Problem 5: Palindrome Checker

**Difficulty:** ⭐⭐⭐ Medium

## Problem Description

Write a program that checks if a word or sentence is a palindrome. A palindrome reads the same forwards and backwards (ignoring spaces and ignoring uppercase/lowercase differences).

## Learning Goals
- Work with strings
- String manipulation (reverse, lowercase, remove spaces)
- Use string methods like `.lower()`, `.replace()`, slicing
- Practice conditional logic

## Hints to Get Started
1. Ask the user to enter a word or sentence
2. Convert to lowercase using `.lower()`
3. Remove all spaces using `.replace(' ', '')`
4. Reverse the string (use slicing: `string[::-1]`)
5. Compare original (cleaned) with reversed version
6. Display if it's a palindrome or not

## Example

**Input:**
```
Enter a word or sentence: racecar
```

**Expected Output:**
```
"racecar" is a PALINDROME
```

**Another Example:**
```
Enter a word or sentence: A man a plan a canal Panama
```

**Expected Output:**
```
"A man a plan a canal Panama" is a PALINDROME
```

**Not a Palindrome Example:**
```
Enter a word or sentence: hello
```

**Expected Output:**
```
"hello" is NOT a palindrome
```

## Tips
- Use `text.lower()` to convert to lowercase
- Use `text.replace(' ', '')` to remove spaces
- Use `text[::-1]` to reverse a string (colon notation!)
- Compare with `==` operator

## Challenge (Optional)
Modify your program to also ignore punctuation marks (!, ?, ., etc.). For example: "Was it a car or a cat I saw?" should be recognized as a palindrome.

Hint: Use `.isalpha()` to check if a character is a letter, and only keep letters.
