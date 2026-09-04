#if elif else statement
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y", f"{x}", "<", f"{y}")
elif x > y:
    print("x is greater than y", f"{x}", ">", f"{y}")
else:
    print("x and y are equal", f"{x}", "==", f"{y}")


# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("They both are equal")

if x !=y:
    print("x is not equal to y")
else:
    print("They both are equal")