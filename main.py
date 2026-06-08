from datetime import datetime

def show_menu():
    print("\n------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter By Category")
    print("4. Exit")

def add_expense():
    amount = input("Enter amount: ").strip()

    print("\nCategories:")
    print("Food")
    print("Transport")
    print("Entertainment")
    print("Other")

    category = input("Enter category: ").strip()
    note = input("Enter note (optional): ").strip()
    if not note:
        note = "N/A"

    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")
    print("Expenses added successfully!")

def view_expenses():
    try:

        with open("expenses.txt", "r") as file:
            total = 0

            print(f"\n{'Date':<15}{'Category':<15}{'Amount':<12}{'Note'}")
            print("-" * 55)

            for line in file:
                if not line.strip():
                    continue
                date, category, amount, note = line.strip().split(",")
                print(f"{date:<15}{category:<15}{amount:<12}{note}")
                total += float(amount)
                
            print("-" * 55)
            print(f"Total expense = {total}")
    except FileNotFoundError:
        print("No expenses found")

def filter_expenses():
    wanted_category = input("Enter category: ").strip()

    try:
        with open("expenses.txt", "r") as file:
            subtotal = 0
            found = False

            print(f"\n{'Date':<15}{'Amount':<12}{'Note'}")
            print("-" * 40)

            for line in file:
                if not line.strip():
                    continue
                date, category, amount, note = line.strip().split(",")
                if category.lower() == wanted_category.lower():
                    print(f"{date:<15}{amount:<12}{note}")
                    subtotal += float(amount)
                    found = True

            if found:
                print("-" * 40)
                print(f"Subtotal = {subtotal}")
            else:
                print("No expenses found in this category")

    except FileNotFoundError:
        print("No expenses found")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()