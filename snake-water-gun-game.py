from operator import truediv
import random  # for using randint function to generate a random number

n = 1
while n > 0:
    # defining gameWin function
    def gameWin(comp, you):
        # if both select same, then tie
        if comp == you:
            return None
    # check all possibilities if computer chose snake
        elif comp == 's':
            if you == 'w':
                return False
            if you == 'g':
                return True
        elif comp == 'w':
            if you == 'g':
                return False
            if you == 's':
                return True
        elif comp == 'g':
            if you == 's':
                return False
            if you == 'w':
                return True

    # generating a random number and storing it in rand var
    rand = random.randint(1, 3)
    if rand == 1:
        comp = 's'
    if rand == 2:
        comp = 'w'
    if rand == 3:
        comp = 'g'

    print("Comp Turn: snake(s), water(w) or gun(g)")

    you = input("Your Turn: snake(s), water(w) or gun(g): ")
    # if you != 's' or you != 'w' or you != 'g':
    #     print("Invalid Choice!\nTry Again!")

    print(f"Comp chose: {comp}")
    print(f"You chose: {you}")

    result = gameWin(comp, you)

    # Finding who won
    if result == None:
        print("It's a tie!")
    if result == True:
        print("You won!")
    if result == False:
        print("You lost!")
