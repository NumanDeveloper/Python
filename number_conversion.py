decimal_number = int(input("Enter decimal value: "))
binary_number = bin(decimal_number)
octal_number = oct(decimal_number)
hex_number = hex(decimal_number)

convert_into = int(input("Convert into: [1] binary, [2] octal, [3] hexadecimal: "))

if convert_into == 1:
    print(f"Converted to binary: {binary_number}")
elif convert_into == 2:
    print(f"Converted to octal: {octal_number}")
elif convert_into == 3:
    print(f"Converted to hexadecimal: {hex_number}")
else:
    print("Invalid Choice!")
