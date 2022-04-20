def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] < array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

data = [3,2,6,7,89,1]
bubble_sort(data)
print(data)