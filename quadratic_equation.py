# This program will check whether the provided equation is quadratic or not
# If so, what are its roots

# Reading a, b and c values
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

# check if quadratic equation
if a == 0:
    print("Not a Quadratic Equation !!\na is zero !!")
else:
    # calculating discriminant 
    disc = b * b - 4*a*c

    # calculating roots.
    x1 = (-b + disc**0.5) / (2*a)
    x2 = (-b - disc**0.5) / (2*a)
    print(f"The roots are {int(x1)} and {int(x2)}.")