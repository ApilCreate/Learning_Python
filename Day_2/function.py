#Function to take input from user and return their name with a greeting

def askName():
    return(input("What's your name? "))

def hello(name="user"):
    print("Hello,", name)

hello()
hello(askName())

#Function to get the square of a number

def num():
    return(int(input("Enter a number: ")))

def calc(n):
    n = n * n
    print("The square is", n)

calc(num())