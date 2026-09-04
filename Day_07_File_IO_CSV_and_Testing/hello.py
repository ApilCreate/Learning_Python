# This function asks the user for their name and prints a greeting.
def main():
    name = input("What's your name? ")
    print(hello(name))

# This function builds the greeting message.
# It takes a name (to) and if nothing is given, it defaults to "world".
# Why: keeping this logic in its own function makes it easy to test
# (see test_hello.py) without needing to type input every time.
def hello(to="world"):
    return f"hello, {to}"

# This makes sure main() only runs when we run this file directly,
# not when it's imported somewhere else (like in the test files).
if __name__ == "__main__":
    main()