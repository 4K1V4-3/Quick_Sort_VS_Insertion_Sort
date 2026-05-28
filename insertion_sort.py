# INSERTION SORT

# arr = [5, 1, 3, 2, 4]

def insertion_sort(arr):
    # Left of 'i' = sorted portion of the array
    # 'i' and on = unsorted portion of the array
    for i in range(1, len(arr)):
        # 'j' will go backwards.
        for j in range(i, 0, -1):   # The '0' is exclusive.
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    
    return arr


# print(insertion_sort(arr))