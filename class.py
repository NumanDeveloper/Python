class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('woof woof')

    def eat(self):
        print("Meat is my fav ❤ food")


fido = Dog("Fido", "black")
fido.bark()
fido.eat()
print(fido.name)
print(Dog.legs)
# print(f"Hey it's {fido.name} having {fido.age} years of age.")
