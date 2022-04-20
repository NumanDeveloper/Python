a = [1, 3, 2, 5, 2, 23, 5, 3]
z = ['e', 'i', 'c', 'r', 't']
# sort() changes the original list
a.sort(reverse=False)
# sorted() doesn't changes the original list and return the sorted list
b = sorted(z)

print(f"list a after sort() function\n{a}")
print(f"list z before sorted() function\n{z}")
print(f"list b after sorted() function\n{b}")