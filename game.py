# Random Number Guessing Game

import random

print('Number Guessing Game')
print("Guess a number between 1 and 10")

number = random.randint(1,10)
chances = 0

while chances < 5:
    guess = int(input("Enter your Guess: "))

    if guess < number:
        print("Guess again. Too low")
    elif guess > number:
        print("Guess again. Too high")
    else:
        print("Congrats, you win! You've guessed the number", guess, "correctly")
        break
    
    chances += 1

if not chances < 5:
    print("Sorry, you lost. The number was", number)