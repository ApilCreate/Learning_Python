def username():
    while True:
        try:
            first_name = input("Enter your first name:")
            last_name = input("Enter your last name:")
            if first_name.isalpha() and last_name.isalpha():
                if len(first_name) <= 2 or len(last_name) <= 2:
                    print("Your name is too short..")
                else:
                    break
        except ValueError:
            print("Enter your proper name")
    
    return first_name, last_name


address = input("Enter your address:")

first_name, last_name = username()
print(f"Hi there! Welcome {first_name} {last_name}. \n{address}")
