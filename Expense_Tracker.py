
expenses = []


def add_expense():
    description = input("Expense description: ")
    amount = float(input("Expense amount: "))
    expenses.append({
        "description": description,
        "amount": amount
    })
    print("Expense added successfully.")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(f"{expense['description']}: {expense['amount']:.2f}")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: {total:.2f}")


def show_average():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
    print(f"Average expense: {average:.2f}")


def main():
    while True:
        print("\n1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")
        print("5. Show average")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            break
        elif choice == "5":
            show_average()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
