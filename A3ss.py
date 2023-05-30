def selectionSort(array, size):
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
        
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
                
         # swapping the elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])

arr_size = int(input("Enter size of array: "))
arr = []

for i in range(arr_size):
    take_user = int(input("Enter value: "))
    arr.append(take_user)

print("\nUnsorted array is: {}".format(arr))
size = len(arr)
selectionSort(arr, size)
print("\nSorted array is: {}".format(arr))
#end-----------------------------------------------------------------------------------------