num = [20,30,40,55,60,65,72,77,88,81,90,96]

print(*(f"{score} is Fail" if score < 40 else f"{score} is Pass" for score in num), sep="\n")

for day in range(1,4):  
    print(f"Day {day}\n")
    for meal in range(1,3):
        print(f"Meal {meal}")

password = "password123"

while True:
    user = input("Enter your password: ")
    if password == user:
        print("Access Granted")
    else:
        print("Incorrect password try again")


