"""
Temperature Converter Program

This module provides functions to convert temperature
between Celsius, Fahrenheit, and Kelvin.
"""


def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Kelvin.
    """
    return celsius + 273.15


def main():
    """
    Main function to run the temperature conversion program.
    """
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit is:", result)

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius is:", result)

    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(celsius)
        print("Temperature in Kelvin is:", result)

    else:
        print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
