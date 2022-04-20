def selection_sort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                t = array[i]
                array[i] = array[j]
                array[j] = t

data = [3,2,6,7,89,1]
selection_sort(data)
print(data)