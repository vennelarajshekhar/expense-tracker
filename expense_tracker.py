expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Your Expenses ---")

    for expense in expenses:
        print(f"{expense['name']} : ₹{expense['amount']}")


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")