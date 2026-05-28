# QUICK SORT

# arr = [4, 2, 7, 5, 8, 1]

def quick_sort(arr):
    # Apply this to original array and subsequent arrays.
    # We'll only apply it if the length of the array or subsequent array is greater than one.
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    lower_than_pivot = []
    higher_than_pivot = []

    for item in arr:
        if item > pivot:
            higher_than_pivot.append(item)
        else:
            lower_than_pivot.append(item)

    # We need to apply this to each subsequent array.
    return quick_sort(lower_than_pivot) + [pivot] + quick_sort(higher_than_pivot)


# print(quick_sort(arr))




