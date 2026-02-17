# Palindrome Checker Program

# Step 1: Ask user to enter a word or sentence
text = input("Enter a word or sentence: ")

# Step 2: Convert to lowercase
text_lower = text.lower()

# Step 3: Remove spaces
text_clean = text_lower.replace(" ", "")

# Step 4: Reverse the string
text_reverse = text_clean[::-1]

# Step 5: Compare original cleaned text with reversed text
if text_clean == text_reverse:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
