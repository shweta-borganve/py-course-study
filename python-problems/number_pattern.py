"""
number_pattern.py

This program takes a number N from the user and displays
different number patterns based on the user's choice:
1 - Ascending (1 to N)
2 - Descending (N to 1)
3 - Reverse using while loop
4 - Multiplication table
"""
N = int(input("Enter a number N: "))

print("\nChoose pattern:")
print("1 - Ascending (1 to N)")
print("2 - Descending (N to 1)")
print("3 - Reverse using while loop")
print("4 - Multiplication table")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Ascending pattern:")
    for i in range(1, N + 1):
        print(i, end=" ")

elif choice == 2:
    print("Descending pattern:")
    for i in range(N, 0, -1):
        print(i, end=" ")

elif choice == 3:
    print("Reverse using while loop:")
    i = N
    while i >= 1:
        print(i, end=" ")
        i -= 1

elif choice == 4:
    print("Multiplication table:")
    for i in range(1, 11):
        print(N, "x", i, "=", N * i)

else:
    print("Invalid choice")
