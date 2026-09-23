from expense import Expense


def main():
    #Take input from the user
    expense = get_user_expense()
    print(expense)
    #Store the expenses into the file
    save_expense_to_file()
    #Read the stored data file amd sumarize expenses
    summarize_expense()

def get_user_expense():
    print("Getting user data..")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter amount costed: "))


    expense_category = [
        "🍔Food", "🏠Home", "👜Work", "🎉Fun", "✨Misc"
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


def save_expense_to_file():
    print("Saving the data into a file..")

def summarize_expense():
    print("Summarizing user's expenses..")

if __name__ == "__main__":
    main()