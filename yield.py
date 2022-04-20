def a():
    for i in range(11):
        return i


y = a()
print(y)

def b():
    for i in y:
        yield i
b = b()
for i in b:
    print(i)
