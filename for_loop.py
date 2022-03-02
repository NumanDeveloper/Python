demo = [1, 3, 5, 6, 7]

for i in demo:
    # in this case, i will refer to elements and not indices
    print(i, end=' ')
print("\n")

for i in range(1, len(demo)+1):
    # in this case, i will refer to indices and not elements
    print(i, end=' ')
