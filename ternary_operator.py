# Use this
def is_even(num):
    print("Even" if num % 2 == 0 else "Odd")
#is_even(3)
# Or this
def is_odd(num):
    print("Odd") if num % 2 != 0 else print("Even")
    
num = int(input('Enter the number to check: '))
is_even(num)
is_odd(num)