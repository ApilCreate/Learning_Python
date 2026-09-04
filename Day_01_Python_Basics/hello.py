# Ask user for their name
# name = input("What's your name? " ) 

#Removes whitespace from str and capitalize
# name = name.strip().title()

#Makes it capital
# name = name.capitalize() Makes the first letter capital
# name = name.title()


name = input("What's your name? " ).strip().title() #All at once 

#Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print("Hello,", name, sep=" ")
print(name) 
print(f"Hello, {first}") # in js we use ``to print a function inside the argument but in python we use letter f


# print('hello, "friend"')
# print("hello, \"friend\"")