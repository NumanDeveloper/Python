def fact_with_for_loop(n):
    fact1 = 1
    # check edge cases 
    if n == 0 or n==1:
        return 1
        
    for i in range(1, n+1):
        fact1 = fact1 * i
    return fact1


print(fact_with_for_loop(4))
