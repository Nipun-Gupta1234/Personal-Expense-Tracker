from datetime import datetime

def show_menu():
    print("\n------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter By Category")
    print("4. Exit")

def add_expense():
    amount=input("Enter amount: ")

    print("\nCategories:")
    print("Food")
    print("Transport")
    print("Entertainment")
    print("Other")

    category=input("Enter category: ")
    note=input("Enter note (optional): ")

    date=datetime.now().strftime("%Y-%m-%d")

    with open("expenses.txt", "a") as file:
        file.write(f"{date}, {category}, {amount}, {note}\n")
    print("Expenses added sucessfully!")

def view_expenses():
    try:
        with open("Expenses.txt", "r") as file:
            total=0

            print("\nDate\t\tCategory\tAmount\tNote")
            print("-"*60)

            for line in file:
                date, category, amount, note=line.strip().split(",")
                print(f"{date}\t{category}\t{amount}\t{note}")
                total+=float(amount)
            print("-"*60)
            print(f"Total expense={total}")
    except FileNotFoundError:
        print("No expenses found")