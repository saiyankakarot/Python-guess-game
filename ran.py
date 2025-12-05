import random

low = 1
high = 6
options = ['rock', 'paper', 'scissors']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', '♠', '♥', '♦', '♣']
number = random.randint(low, high)
number = random.random()
# number = str(number)
random.shuffle(cards)

#random.shuffle(options)
# options = random.choice(options)
# print(number)
# print(options)
print(cards)