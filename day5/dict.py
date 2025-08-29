name = {"India":"Delhi", "Japan":"Tokyo"} 
country = (input("Enter the country: ")) 

if country in name:
    print(f"the capital of {country} is {name[country]} ")
else:
    print("Sorry,country not found in dict") 