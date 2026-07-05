# names = []

# for _ in range(3):
#     #adds one item to the end of a list.
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What is your name? ")

# #open file and write value inside the file
# with open("names.txt", "a") as file:
#     #or
#     # file = open("names.txt", "a")
#     file.write(f"{name}\n")
    # file.close()

# reads a exsiting file

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip()) 

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())



names = sorted(names)

for name in names:
    print(f"hello, {name}")

