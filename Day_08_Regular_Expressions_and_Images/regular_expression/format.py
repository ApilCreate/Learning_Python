import re

name = input("What's your name? ").strip()

#This is a walrus operator, which means it combines two things:
#First with this i can store something in my variable and can do a if else condition in a single line 
if matches := re.search(r"^(.+), *(.+)$", name):

    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")