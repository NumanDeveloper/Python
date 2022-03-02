def fact_with_while_loop(n):
    fact = 1
    # check edge cases 
    if n == 0 or n==1:
        return 1
        
    while n != 0:
        fact *= n
        n-=1
    return fact


print(fact_with_while_loop(3))