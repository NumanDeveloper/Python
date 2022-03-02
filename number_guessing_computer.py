# This is a number guessing game
import random


def guess():
    print("-----Welcome to Number Guessing Game-----\nThink of a number between 1 and 5\nComputer will guess your number😉")
    feedback = ''
    while feedback != 'c':
        num = random.randint(1, 6)
        print(f"\nComputer guessed: {num}. Is this correct?")
        feedback = input('Too high (H), Too low (L), Correct (C)').lower()
    print('Computer gessed it')


guess()
