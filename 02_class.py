while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter a real number.")
print(number)
