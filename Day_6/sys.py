import sys

if len(sys.argv) < 2:
    sys.exit("Too many arguments")


#1: means start at index 1 and : this means till the end
for arg in sys.argv[1:]:
    print("Hello, my name is ", arg)