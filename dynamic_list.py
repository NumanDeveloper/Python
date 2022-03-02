# this list will be created dynamically based on the condition that we provided
from traceback import print_tb


a = [k for k in range(11) if k % 4 == 0]
print(a)

b = {k for k in range(11)}
print(b)

d = {1:k for k in range(6)}
print(d)

x = [1,3,5,3,5,1]
print(f"List: {x}")
y = set(x)
print(f"List converted to set: {y}")

dic = {1:3, 2:6, 3:9,}
print(f"Dictionary: {dic}")
print(f"Dict to set: {set(dic)}")
print(f"Dict to list: {list(dic)}")
print(f"Dict to tuple: {tuple(dic)}")