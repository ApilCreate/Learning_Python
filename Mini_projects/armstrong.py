# Armstrong Number Checker
# Build: a program that takes a number and tells you if it's an Armstrong number.


while True:
    try:
        x = int(input("Enter the number you want to check: "))
        break
    except ValueError:
        print("Invalid value, please enter a valid number")
    

print("Ohhh so you choose", x, "Let's check it")

digits  = []

def process(num):
    compare = num
    total = 0
    power = len(str(compare))

    while num > 0 :
        digit = num % 10
        digits.append(digit)
        total += digit ** power
        num //= 10

    if compare == total:
        print(f"Well done, {compare} is an armstrong number....")
    else :
        print(f"{compare} is not an armstrong number")

    retry()

def retry():
    print("Wanna check again?")

    while True:
        ask = input(f"Enter Y to check again or Enter N to exit: ")
        if ask.lower() not in ["y","n"]:
            print("Incorrect retry")
            continue
        else:
            break
    
    if ask.lower() == 'y':
        y = int(input("Enter the number you want to check: "))
        return process(y)
    else:
        print("Thank you, do visit again...")


process(x)

