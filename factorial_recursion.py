def fact(n):
    # check edge cases
    if n == 0 or n == 1:
        return 1

    # n*n-1*n-2*n-3*...*3*2*1
    return n * fact(n-1)


print(fact(5))
