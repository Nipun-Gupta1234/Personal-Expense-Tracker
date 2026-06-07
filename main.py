from datetime import datetime

def show_menu():
    print("\n------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter By Category")
    print("4. Exit")

def main():
    while True:
        show_menu()

        choice=input("Enter choice: ")

        if choice=="4":
            print("Exiting")
            break

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