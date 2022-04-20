print("-----Welcome to CASH COUNTER-----")

'''
The motivation of this program is the cash counting machines found in banks
'''
while True:
    note = int(input("Enter rupees of single note: "))
    num = int(input("Enter number of notes: "))
    print(f"There are {note*num} rupees in total!\n")
