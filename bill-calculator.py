'''
I am making a bill calculator app
'''
'''
Logic:
1. Enter name of comodity
2. Enter price of comodity
3. Display name and price of that comodity
4. Add price to the total bill
5. Continue until user presses 'q'
6. Display # of items and Grand Total
'''

sum = 0  # for sum
totalComodities = 0  # for counting comodities
while(True):
    comodityName = input("Enter the name of comodity or enter q for quit: ")
    if(comodityName != 'q'):
        comodityPrice = input(f"Enter the price of {comodityName}: ")
        # for i in range(1, 50):
        print(f"{comodityName}: {comodityPrice}")
        # remember to typecast comodityPrice into int 
        sum = sum + int(comodityPrice)
        print(f"Total Bill so far: {sum}")
        totalComodities += 1
    else:
        print(f"You bought {totalComodities} items \nGrand Total: {sum}")
        break
