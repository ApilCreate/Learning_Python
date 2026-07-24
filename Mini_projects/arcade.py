import sys
from guess_number import main
from rps import run


try:
    username = sys.argv[1]

    if len(username) > 2:
        print(f"{username}, welcome to the Arcade!! 🤖🤖.\n ")
    else:
        print("Enter a valid username")
except IndexError:
    print("\nEnter your name right after calling the file ok... \n\n e.g. python arcade.py 'Your name here...' \n")
    sys.exit()

print("So which game do you wanna play?")

print("1 = Rock Paper Scissor Game")
print("2 = Number Guessing Game")
print("Press 'x' to exit the arcade")

user_response = input("").strip().lower()

if user_response == '1':
    run()
elif user_response == '2':
    main()
elif user_response == 'x':
    print("\nThank you, visit again....\n\n")
else:
    print("Please choose 1, 2, or x")


