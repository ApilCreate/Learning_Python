def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number.")


def interactive_menu(num1, num2):
    options = ["Add", "Subtract", "Multiply", "Divide"]

    print("Select your function to do:")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    try:
        menu_entry_index = int(input("Choose an option: ")) - 1
    except ValueError:
        print("Invalid selection.")
        return

    if menu_entry_index < 0 or menu_entry_index >= len(options):
        print("Invalid selection.")
        return

    selection = options[menu_entry_index]
    print(f"You selected: {selection}")

    if selection == "Add":
        print(num1 + num2)
    elif selection == "Subtract":
        print(num1 - num2)
    elif selection == "Multiply":
        print(num1 * num2)
    elif selection == "Divide":
        print(num1 / num2)


num1 = get_number("Enter a number: ")
num2 = get_number("Enter another number: ")
interactive_menu(num1, num2)


