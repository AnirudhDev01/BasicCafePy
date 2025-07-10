# Python Cafe Ordering System

This simple Python program simulates an ordering system for a cafe. It was created by **Anirudh** as a beginner-friendly project using Python dictionaries and basic input/output handling.

## 🧾 How it Works

1. The menu is stored in a dictionary where:
   - The **keys** are the names of the items (e.g., `"Salad"`).
   - The **values** are the prices of the items (e.g., `40` for Salad).

2. The program:
   - Welcomes the user.
   - Displays a menu of 4 items with prices.
   - Asks the user to input the name of the first item they'd like to order.
   - Checks if the item exists in the menu:
     - If it does, it adds the item's price to the total bill.
     - If not, it shows an "Item not found" message.
   - Asks the user if they want to order another item.
     - If yes, it repeats the process for the second item.
     - If no, it simply shows the final total.

3. Finally, the total bill is displayed and the program thanks the user.

## 🧠 Concepts Used

- Python dictionaries
- Conditional statements (`if`, `else`, `elif`)
- User input handling (`input()`)
- String formatting with `f-strings`

## 💡 Example Usage

Welcome to Python Cafe<br>
Our Menu:<br>
1.Salad:Rs40<br>
2.Coffee:Rs50<br>
3.Bread:Rs30<br>
4.Milk:Rs40<br><br>
Enter item from menu to order: Coffee<br>
Your item Coffee has been added<br>
Do you want to add any other item? (Y/N): Y<br>
Enter another item to add: Bread<br>
Your item Bread has been added<br>
Thank you visit again!<br>
Your total is: 80


## ✅ Future Improvements

- Allow multiple items and quantities.
- Handle case-insensitive inputs.
- Use numbers (1-4) to select items instead of names.
- Loop until the user decides to finish the order.

---

Created by **Anirudh**