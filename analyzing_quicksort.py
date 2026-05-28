# 1. Call quick_sort() on the array.
# 2. Base case: If the length of the array is 1 or less, return the arr to whichever quick_sort() call called it.
# 3. Make the last element into the pivot.
# 4. Iterate through the array or subarray. 
# 5. If an element is lower than the pivot, it is placed to the left of the pivot. If an element is greater than the pivot, it is placed to the right of the pivot.
# 6. The proper place for the pivot has been located. Now, we'll recursively find the correct place for the pivot in the left and right subarrays.
# 7. Create left and right arrays. Store the elements to the left of the pivot in the left array, and the elements to the right of the pivot in the right array.
# 8. Call quick_sort() on the left array, concatenate the pivot, and call quick_sort() on the right array.
# 9. Eventually, the array will be filled with pivots that have all found their proper positions.
# 10. Return the pivot-filled array.