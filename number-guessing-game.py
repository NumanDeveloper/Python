# ---This is a number guessing game---

'''
Logic:
1. Generate a random number between 1 and 50 using random module
2. Let the user guess that nunmber
3. Case 1: User guesses right
4. Case 2: User guesses a smaller number
5. Case 3: User guesses a larger number
6. Game should be repetitive
7. Count the number of guesses
'''

# generating a random number
from os import read
import random

print("*** Welcome to the Number Guessing Game ***")
randomNumber = random.randint(1, 50)
# print(randomNumber)

userGuess = None  # bcz userGuess has not initiated yet
guesses = 0
while(userGuess != randomNumber):
    userGuess = int(input("Guess the number buddy(1 to 50): "))
    if(userGuess < 1 or userGuess > 50):
        print("Invalid Number!")
        continue
    if(userGuess == randomNumber):
        print("************************************")
        print("Congrats! You guessed it right buddy")
    else:
        # if guess is wrong
        if(userGuess < randomNumber):
            print("Wrong! Guess a bigger number")
        else:
            print("Wrong! Guess a smaller number")
    guesses += 1

print(f"You hit right in {guesses} guesses")
print("************************************")
# open the file in read mode
with open("high-score.txt", "r") as f:
    # read the score in file
    highScore = int(f.read())

if(guesses < highScore):
    print("You have just broke the previous high score")
    # print("*******************************************")
    # open the file in write mode
    with open("high-score.txt", "w") as f:
        # write the new high score in file
        f.write(str(guesses))
