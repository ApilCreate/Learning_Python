# This function asks the user for a number and prints its square.
def main():
    x =int(input("What's x? "))
    print("x square is", square(x))

# This function squares a number (multiplies it by itself).
# Why: it's kept separate from main() so it can be tested on its own
# with different values (see test_calculator.py) without user input.
def square(n):
    return n * n


# Only run main() when this file is executed directly,
# not when it's imported (e.g. by a test file).
if __name__ == "__main__":
    main()