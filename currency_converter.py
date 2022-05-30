# This program will calculate # of trailing zeros in the factorial of a given number
'''
Logic:
1. Calculate the factorial of a given number
2. Calculate the # of trailing zeros in that factorial
3. Print the trailing zeros
'''


# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return number * factorial(number-1)


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)


def factorialTrailingZeroes(number):
    #fac = factorial(number)
    # print(fac)
    count = 0
    i = 5
    while (number//i != 0):
        count += number//i
        i = i*5
    return count
    # while (fac%10 ==0):
    #count = count+1
    #fac = fac/10
    # return count


if __name__ == '__main__':
    number = int(input("Enter a number: \n"))
    #fac = factorial(number)
    #print(f'The factorial is {fac}')
    print(factorialTrailingZeroes(number))


# n = int(print("Enter a number: "))
# fact = factorial(n)


# def trailingZeros(fact):
#     # Logic: # of trailing zeros will be equal to 5*2s in the factorial
#     # so we will find # of 5s in the factorial and hence the trailing zeros
#     count = 0
#     i = 5
#     while(fact//i != 0):  # loop will continue till number becomes less than 5
#         count += int(fact/i)
#         i = i*5
#         return count


# # number = print("Enter a number: ")
# trailingZeros(fact)
