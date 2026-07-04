# Takes a name and prints a greeting for it
def hello(name):
    print(f"hello, {name}" )

# Takes a name and prints a farewell for it
def goodbye(name):
    print(f"goodbye, {name}")


def main():
    hello("world")
    goodbye("world")


# __name__ is a special variable Python sets for every file:
# it's "__main__" when this file is run directly, or "sayings" when it's imported.
# So this only runs main() when this file is executed directly,
# not when it's imported by another script (like mySay.py)
if __name__ == "__main__":
    main()