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

# This is the "active" version of the code below — the commented-out
# blocks above are earlier drafts/experiments kept for reference.
names = []

# Open names.txt for reading (default mode "r") and read it line by line.
# Why use "with": it automatically closes the file for us when done,
# even if an error happens, so we don't have to call file.close() ourselves.
with open("names.txt") as file:
    for line in file:
        # rstrip() removes the trailing "\n" newline character each line
        # ends with, so it doesn't get printed later.
        names.append(line.rstrip())


# sorted(..., reverse=True) returns a new list sorted Z to A instead of A to Z.
names = sorted(names, reverse=True)

for name in names:
    print(f"hello, {name}")

