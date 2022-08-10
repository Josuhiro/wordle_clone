from termcolor import colored
import random

with open("words.txt", "r") as f:
    words = f.read().splitlines()

word = random.choice(words).lower()
attempt = 0
print("Enter 5 letter word:")

while True:
    guess = input().lower()
    if len(guess) != 5:
        print("Please enter 5 letter word")
    else:
        if guess == word:
            print(colored('You won!', 'green'))
            break
        for i in range(len(word)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(colored(guess[i], 'red'), end="")
        print(f"\n{5 - attempt} attempts left")
        attempt += 1
        if attempt == 6:
            print(colored(f"You lost, the correct word was {word}", 'red'))
            break
