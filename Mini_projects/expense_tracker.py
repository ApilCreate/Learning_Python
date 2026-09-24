from expense import Expense
from pathlib import Path


def main():

    expense_file_path = Path(__file__).with_name("expenses.csv")
    #Take input from the user
    expense = get_user_expense()
    #Store the expenses into the file
    #save_expense_to_file(expense, expense_file_path)
    #Read the stored data file amd sumarize expenses
    summarize_expense(expense_file_path)

def get_user_expense():
    print("Getting user data..")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter amount costed: "))


    expense_category = [
        "🍔 Food", "🏠 Home", "👜 Work", "🎉 Fun", "✨ Misc"
    ]

    while True:
        print("Select a category: ")

        for index, category in enumerate(expense_category):
            print(f"{index + 1}: {category}")

        value_range = f"[1 - {len(expense_category)}]"

        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

            if selected_index in range(len(expense_category)):
                selected_category = expense_category[selected_index]
                new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
                return new_expense
            else:
                print("Invalid!! Please try again")

        except ValueError:
            print("Invalid!! Please enter a number only")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path):
    print("Summarizing user's expenses..")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        for line in f:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category")
    for key, amount in amount_by_category.items():
        print(f"  {key}: Rs.{amount:.2f}")


if __name__ == "__main__":
    main()