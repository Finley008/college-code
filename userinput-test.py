# This program asks the user to choose a drink from a list of options and prints the selected drink.
# The user is prompted to enter a number corresponding to their choice.

import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')

# Example usage:
clear_screen()

print("Welcome to the drink vending machine")
print("We have the following drinks:")
print("1. fanta")
print("2. 7Up")
print("3. dr pepper")
print("4. diet coke")
print("Please select a number from the list above")
choice = input("Which drink would you like? (1/2/3/4) ")

drinks = {
    "1": "fanta",
    "2": "7Up", 
    "3": "dr pepper",
    "4": "diet coke"
}

if choice == "1":
    print(f"You chose {drinks['1']}")
elif choice == "2":
    print(f"You chose {drinks['2']}")
elif choice == "3":
    print(f"You chose {drinks['3']}")
elif choice == "4":
    print(f"You chose {drinks['4']}")
else:
    print("Please select a valid product")
