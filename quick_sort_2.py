# Another implementation of QUICK SORT.
# Here, we use indexes instead of passing in the actual array or subarray.


arr = [4, 2, 7, 1, 8, 5]


def partition(arr, low, high):  # (arr, 0, 6)
    # If an element is less than the pivot, we keep it on the left of the pivot.
    # If an element is greater that the pivot, we freeze 'i'. 
    pivot = arr[high]       
    i = low - 1             
    for j in range(low, high):      
        if arr[j] <= pivot:     # If element is less than the pivot.
            i += 1              
            arr[i], arr[j] = arr[j], arr[i]     # Swap it to the left of the pivot. 
        # else: Freeze 'i' to the current element. 'i' does not update. When we once again reach an element that is less than or equal to the pivot, we swap that element with the frozen 'i'.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]   # Finally, put the pivot in its proper place.       
                                                    # Swap the pivot with the element in the spot that is right after the last element that we found to be less than the pivot. This puts the pivot just ahead of the elements less than it, and just before the elements greater than it.      
                                                    # This is where the array updates.
    # 'arr' is updated, and we also return the partition.
    return i + 1    # Index of the partition.


def quick_sort(arr, low, high):         # Takes array,    
    if low < high:                       # 0 or 1 elements in the array.    # For an array of one element, the partition is that element.
        p = partition(arr, low, high)   # (arr, 0, 6)   # Returns '5'.
        # We found the proper place for the pivot. We return index of the pivot.
        quick_sort(arr, low, p - 1)     # Array of elements less than the pivot which are on the left.
        quick_sort(arr, p + 1, high)    # Array of elements greater than the pivot which are on the right.


quick_sort(arr, 0, len(arr) - 1)    # Pass in the array, the index of the first element, and the index of the last element.
print(arr)