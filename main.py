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

main()