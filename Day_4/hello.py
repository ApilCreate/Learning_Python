# x = int(input("What's x? "))
# print(f"x is {x}")

#using try, except and else
#Here try means the actual code to run but what if user gives a different input which he is not supposed to give, like instead if number he gives a name.
#Here's where the try except is used:
#Inside try the acutal code is runned, and lets say the result comes with a ValueError, here's where except ValueError comes.  
# try:
#     x = int(input("What's x? "))
# #If the result is ValueError, then the following print statement or command will execute.
# except ValueError:
#     print("x is not an integer")
# #Here else means first the code will try to run line 9, if it successed then line 15 will run. But if the code gets a ValueError then line 12 will run.
# else:
#     print(f"x is {x}")


#Looping 

# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()