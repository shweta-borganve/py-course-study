# Dictionary of countries and capitals
countries = {"India": "New Delhi", "Japan": "Tokyo"}

# Ask user for a country
country = input("Enter a country name: ")

# Print the capital if country is found
if country in countries:
    print(f"The capital of {country} is {countries[country]}.")
else:
    print("Sorry, that country is not in the list.")
