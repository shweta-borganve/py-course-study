"""
List Analyzer Program.

This program:
- Takes numbers separated by commas as input
- Finds largest and smallest number
- Calculates average
- Counts even and odd numbers
"""


def main():
    """Main function to execute list analyzer program."""
    # Step 1: Take input from user
    user_input = input("Enter numbers separated by commas: ")

    # Step 2: Convert input string to list of numbers
    num_list = user_input.split(",")

    numbers = []
    for value in num_list:
        numbers.append(int(value.strip()))

    # Step 3: Find largest and smallest
    largest = max(numbers)
    smallest = min(numbers)

    # Step 4: Find average
    total = sum(numbers)
    average = total / len(numbers)

    # Step 5: Count even and odd
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Step 6: Display results
    print("Largest number:", largest)
    print("Smallest number:", smallest)
    print("Average:", average)
    print("Even numbers count:", even_count)
    print("Odd numbers count:", odd_count)


if __name__ == "__main__":
    main()
