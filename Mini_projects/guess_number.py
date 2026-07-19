# Process 3 numbers, take input from user, if guess == user input then declare winner. If asked to play again then start over otherwise end.
import sys
import random

def name_check():
    x = input("Hi player, what to call you by?")
    if len(x) <= 2:
        print("Enter your real name, name is to short")
        sys.exit()
    return x

def choose_check():
    y = sys.argv[1]
    if y not in ["1", "2", "3"]:
        print("Please choose a number between 1, 2 or 3")
        sys.exit()
    return y


shuffle = random.choice([1,2,3])
name = name_check()

def process():
    if int(choose_check()) == shuffle:
        print("Congratulations you guessed it right!!")
    else:
        print(f"Bad luck, it was {shuffle}. Don't worry there's always a next time!")

def play_again():
        print("Wanna play again?")

        while True:
            playagain = input("Enter 'Y' to play again or enter 'N' to quit the game")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            sys.argv[1] = input("Choose a new number between 1, 2 and 3")
            return game()
        else:
            print(f"Thank you {name} for playing")
            print("Do come back again")

def game():
        choose = choose_check()
        print(f"Hi {name}, this is a guessing game. You will need to guess a number between 1..,2.., and 3..")
        print(f"You have choosen {choose}. Let's see if you won")
        process()
        print(sys.argv[1])
        play_again()

def main():
    game()

main()







