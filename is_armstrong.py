""" * Armstrong Number Checker * """
"""
 * A number is armstrong if the sum of cube of its digits is equal to the number
 * itself.
"""


def isArmstrong(n):
    sum = 0
    t = n

    while (t > 0):
        d = t % 10
        sum = sum + (d * d * d)
        t = t // 10

    if (sum == n):
        return True

    return False


# Driver Code
print("Armstrong" if isArmstrong(123) else "Not Armstrong")
