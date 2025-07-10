# This program is built by Anirudh
# Define the menu using a dictionary: keys are item numbers, values are (item name, price)
menu = {
    1: ("Salad",40),
    2: ("Coffee",50),
    3: ("Bread",30),
    4: ("Milk",40)
}

# Display welcome message and menu
print("Welcome to Python Cafe")
print("Our Menu:")
for key,value in menu.items():
    print(f"{key}. {value[0]}: Rs.{value[1]}")


# Initialize the total amount
total_amount = 0

# Take first item input from user
item_1 = int(input("Enter the item number you want to order: "))
if item_1 in menu:
    total_amount+=menu[item_1][1]
    print(f"Your item {menu[item_1][0]} has been added to the cart")
else:
    print("Please enter valid number between 1 to 4")
 
# Ask user if they want to add another item    
q = input("Do you want to add any other item to the cart? (Y/N): ").strip().upper()

# If user wants to stop ordering

if q == "N":
    print(f"Your total is: {total_amount}")

# If user wants to add one more item    

elif q == "Y":
    item_2 = int(input("Enter the item number you want to order: "))
    if item_2 in menu:
        print(f"Your item {menu[item_2][0]} has been added to the cart")
        total_amount+=menu[item_2][1]
    else:
        print("Please enter valid number between 1 to 4")
# Display the final total and thank-you message
print(f"Thank you visit again!\nYour total is: {total_amount}")