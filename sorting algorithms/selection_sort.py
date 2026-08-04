def selectionSort(array, size):
    for ind in range(size - 1):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        array[ind], array[min_index] = array[min_index], array[ind]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)

print(arr)
'''
TC:
BC - O(n^2)
AC - O(n^2)
WC - O(n^2)

SC:
BC - O(1)
AC - O(1)
WC - O(1)
'''
