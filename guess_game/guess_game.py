# Guessing Game.
import random
data = random.randint(1, 20)

def guess_game():
    guess_count = 1
    guess_limit = 3
    while guess_count <= guess_limit:
        guess = int(input("Guess mystery number: "))
        guess_count += 1
        if guess == data:
            print('You Won!')
        elif guess > data:
            print("You guessed too high")
        else:
            print("You guessed too low")

guess_game()
