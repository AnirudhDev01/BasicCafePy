# This program is built by Anirudh

# A dictionary named 'menu' is created where:
# - Keys are the item names (as strings)
# - Values are the item prices (as integers)
menu = {
    'Salad': 40,
    'Coffee': 50,
    'Bread': 30,
    'Milk': 20
}

# Display welcome message and menu
print("Welcome to Python Cafe")
print("Our Menu:\n1.Salad:Rs40\n2.Coffee:Rs50\n3.Bread:Rs30\n4.Milk:Rs40")

# Variable to keep track of the total amount
total_amount = 0

# Take first item input from the user
item_1 = input("Enter item from menu to order")

# Check if the item is in the menu
if item_1 in menu:
    # If valid, add its price to total and confirm addition
    print(f"Your item {item_1} has been added")
    total_amount += menu[item_1]
else:
    # If item is not in the menu, show error message
    print("Item not found")

# Ask if user wants to add another item
q = input("Do you want to add any other item? (Y/N)")

# If user says no, show total
if q == "N":
    print("Your total is: ", total_amount)
elif q == "Y":
    # If yes, take another item input
    item_2 = input("Enter another item to add")
    if item_2 in menu:
        # If valid, add its price to total and confirm addition
        print(f"Your item {item_2} has been added")
        total_amount += menu[item_2]
    else:
        # If not valid, show error
        print(f"{item_2} not in the menu")

# Print final thank you and total bill
print("Thank you visit again!\nYour total is: ", total_amount)
