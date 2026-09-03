import importlib
#Used importlib because the module name is 01_class which means it has a number, for imports numbers are not valid.

user_details = importlib.import_module("01_class")


while True:
    try:
        number = int(input("Enter your age: "))
        break
    except ValueError:
        print("Enter a real number.")


first_name, last_name = user_details.username()
address = user_details.get_address()
print(f"Hi there! Welcome {first_name} {last_name}. \n{address}")
print(number)

