#Palindrome checker

while True:
    try:
        char = input("Enter the leter that you want to check: ").lower()
        if char.isalpha():
            break
    except ValueError:
        print("Invalid input please retype to appropriate value")
        continue


while True:
    try:
        num = int(input("Enter the number that you want to check: "))
        break
    except ValueError:
        print("Invalid input please retype to appropriate value")
        continue

string = str(num)
reverse = string[::-1]
integer = int(reverse)

char_reverse = char[::-1]

if char == char_reverse:
    print(f"{char} is a palindrome character")
else:
    print(f"{char} is not a palindrome character") 

if num == integer:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number") 

