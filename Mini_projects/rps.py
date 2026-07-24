import random


def run():
    def user():
        print("Choice:")
        print("1 = Rock")
        print("2 = Paper")
        print("3 = Scissor")
        print("Or press 'x' to exit the game")

        user_choose = input("").strip().lower()
        return user_choose

    def computer():
        choices = ['rock', 'paper', 'scissor']
        computer_choose = random.choice(choices)
        print("The computer has made his choice!!!")
        return computer_choose

    user_choice = user()

    if user_choice == 'x':
        return "Thanks you, let's play next time!!!"
    
    if user_choice == '1' and computer() == 'paper':
        return "Computer is the winner"
    elif user_choice == '2' and computer() == 'scissor':
        return "Computer is the winner"
    elif user_choice == '3' and computer() == 'rock':
        return "Computer is the winner"
    else:
        return "User has won the match!!!!!!!!!🥳🥳🎉🎉🎉"


print(run())

