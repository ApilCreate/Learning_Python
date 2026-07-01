#while loop
# i = 0
# n = int(input("Enter a number:"))
# while i != n:
#     print("meow")
#     i = i + 1


#for loop
# for i in range(5):
#     print("meow")


# python way of printing the things xtimes 
# print("meow\n" * 3, end="") #here end="" means leaving a blank result after *3 is completed


# writing loop where user is asked to tell how many times will the loop run
# while True:
#     n = int(input("What's n?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def askedValue():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    
    return n

def printingText(a):
    print("Meow\n" * a, end="")

printingText(askedValue())

