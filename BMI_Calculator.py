'''
Making a BMI calculator. It takes weight in kg and height in metre and calculate bmi
it also tell about your health condition

Logic:
Calculate the BMI using the formula weight/(height*height)
Check the condition of health using conditionals
'''

# Taking user input
name = input("Enter your good name: ")
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your hieght in meters: "))

# Calculating BMI
BMI = weight/(height*height)

# Checking condition of health
if BMI < 18:
    print(f"Dear {name}")
    print("Yor are Underweight\nGet some healthy diet")

if BMI >= 18 and BMI < 25:
    print(f"Dear {name}")
    print("Your are Normal\nHave fun and keep enjoying your life")

if BMI >= 25 and BMI < 30:
    print(f"Dear {name}")
    print("You are Overweight\nHave some tight exercise and eating habit")

if BMI >= 30:
    print(f"Dear {name}")
    print("You have Obesity\nKeep yourself away from fast food and over-eating")
