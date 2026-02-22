"""
Temperature Conversion Program

This module provides functions to convert temperatures
between Celsius, Fahrenheit, and Kelvin.
"""
# Temperature Conversion Program

# Function 1: Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature converted to Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Function 2: Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Function 3: Celsius to Kelvin
def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature converted to Kelvin.
    """
    kelvin = celsius + 273.15
    return kelvin


# Main Program
def main():
    """
    Display menu and perform temperature conversion
    based on user choice.
    """
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit is:", result)

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(f)
        print("Temperature in Celsius is:", result)

    elif choice == "3":
        c = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(c)
        print("Temperature in Kelvin is:", result)

    else:
        print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(c)
    print("Temperature in Fahrenheit is:", result)

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(f)
    print("Temperature in Celsius is:", result)

elif choice == "3":
    c = float(input("Enter temperature in Celsius: "))
    result = celsius_to_kelvin(c)
    print("Temperature in Kelvin is:", result)

else:
    print("Invalid choice! Please select 1, 2, or 3.")
