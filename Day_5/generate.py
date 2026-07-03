import random

#Gives probability of getting a answer randomly
coin = random.choice(["heads", "tails"])
print(coin)

#Randomly gives a number which starts from 1 and ends at 10 
number = random.randint(1,10)
print(number)

cards = ["jack","queen","king","ace"]
#Shuffels the elements from the list 
random.shuffle(cards)

print(cards)

for card in cards:
    print(card)