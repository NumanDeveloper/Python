def factorial(number):
    '''This is a recursive function that continuously calls itself until the number becomes 1 or 0. Then, it returns the answer by multiplying all the numbers'''
    if (number == 0 or number == 1):
        return 1
    return (number * factorial(number - 1))


# Driver code
number = int(input("Enter number: "))
print(f"The factorial of {number} is {factorial(number)}")