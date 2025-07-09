# This program is built by Anirudh
# Here the program uses python dictionaries (key - item_name, value-item_price) to store the items of a simple cafe
# The user has to enter the name of the item such as Salad to order it 
# if item is not present it shows message "Item not found"
# The user is asked for second time if he wants to add something
# Similar procedure is for ordering the second item which is last in this case
# The total amount user has to pay according to menu is displayed at end of the program  
menu = {
    'Salad': 40,
    'Coffee': 50,
    'Bread': 30,
    'Milk': 20
}
print("Welcome to Python Cafe")
print("Our Menu:\n1.Salad:Rs40\n2.Coffee:Rs50\n3.Bread:Rs30\n4.Milk:Rs40")
total_amount = 0
item_1 = input("Enter item from menu to order")
if item_1 in menu:
    print(f"Your item {item_1} has been added")
    total_amount+= menu[item_1]
else:
    print("Item not found")
q = input("Do you want to add any other item? (Y/N)")
if q == "N":
    print("Your total is: ",total_amount)
elif q == "Y":
    item_2 = input("Enter another item to add")
    if item_2 in menu:
        print(f"Your item {item_2} has been added")
        total_amount+=menu[item_2]
    else:
        print(f"{item_2} not in the menu")
print("Thank you visit again!\nYour total is: ",total_amount)