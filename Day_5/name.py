# sys is a toolbox that lets us read what you typed after "python name.py"
import sys

# print("hello, my name is", sys.argv[1])


# This function tries to grab the name you typed on the command line
def name():
    try:
        # sys.argv is a list of words you typed. argv[1] is the 2nd word (the name!)
        return sys.argv[1]
    except IndexError:
        # If there was no 2nd word, Python gets confused and this runs instead
        print("Please type your name also with a space")
        # This is like pressing STOP - the whole program shuts down right here
        sys.exit(1)


# This function checks if the name you gave is a real, long-enough name
def check():
    x = name()  # ask name() to go get the name first
    if len(x) <= 2:
        # len(x) counts the letters. 2 or fewer letters = too short to be a name
        print("Enter your real name!!! ")
        sys.exit(1)  # STOP again, because the name was too short
    else:
        return x  # the name was good, so hand it back


# This function is like the boss - it calls the other functions and says hi
def main():
    actualName = check()  # ask check() for a good name
    print(f"hi {actualName}")  # say hello using that name


# This is the line that actually starts everything running
main()
