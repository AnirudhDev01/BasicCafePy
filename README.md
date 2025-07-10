# 🏪 Python Cafe Ordering System

This Python project simulates a simple cafe ordering system. It was created by **Anirudh** as a beginner-friendly project to practice Python basics like dictionaries, conditionals, and input handling.

---

## 📁 Files Included

### ✅ `cafe.py` – Original Version

The initial version of the cafe ordering program.

**Key Features:**
- Menu stored using **item names as keys** (e.g., `'Salad': 40`)
- User enters **item names** to place an order
- Supports adding **up to two items**
- Basic input checking and total calculation

---

### 🚀 `cafev2.py` – Updated Version

This improved version enhances the original with better structure and user experience.

**🔧 Key Improvements:**
- Menu uses **item numbers as keys** and tuples for values  
  *(e.g., `{1: ("Salad", 40), 2: ("Coffee", 50)}`)*
- User selects items using **numbers instead of names**
- Enhanced **input validation** with clearer feedback
- Improved formatting and user interaction flow
- Code is more readable and beginner-friendly

---

## 🧾 How it Works (in `cafev2.py`)

1. Displays a numbered menu with item names and prices.
2. Prompts user to enter an item number to order.
3. Validates selection and adds price to total bill.
4. Asks if the user wants to add another item.
5. Displays final total and thank-you message.

---

## 💡 Example Output

Welcome to Python Cafe<br>
Our Menu:<br>

1.Salad: Rs.40
2.Coffee: Rs.50
3.Bread: Rs.30
4.Milk: Rs.40
<br>
Enter the item number you want to order: 2<br>
Your item Coffee has been added to the cart<br>
Do you want to add any other item to the cart? (Y/N): Y<br>
Enter the item number you want to order: 3<br>
Your item Bread has been added to the cart<br>
Thank you visit again!<br>
Your total is: 80<br>

---

## 🧠 Concepts Used

- Python dictionaries (with both string and integer keys)
- Tuples to store item name and price
- Conditional statements (`if`, `else`, `elif`)
- User input and basic validation
- Formatted output using `f-strings`

---

## 🚧 Future Improvements

- Allow unlimited items via a loop
- Add quantity input per item
- Handle invalid/non-integer inputs gracefully
- Support case-insensitive item names in `cafe.py`

---

👨‍💻 Created by **Anirudh**