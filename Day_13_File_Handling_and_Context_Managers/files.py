import os
# r = Read
# a = Append
# w = Write
# x = Create

#Read - error if it doesnot exist

f = open("names.txt", "rt")#r means read and t means text file

# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()


# Append - creates the file if it doesn't exist

with open("names.txt", "a") as a:
    a.write("\nYAS")


#Write (overwrite)

with open("context.txt", "w") as w:
    w.write("I deleted all of its context")

#Two ways to create new file

#Opens a file for writing, creats the file if it does not exist

f = open("names_new.txt", "w")
f.close()

#Creates the specified file, but returns an error if the file exsits 
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

#Delete a file

#avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file does not exist")