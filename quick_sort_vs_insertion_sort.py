# Useful demonstration of Quick Sort.

# What is Quick Sort useful for in real life?
# Useful for sorting very large data.

from quick_sort_1 import quick_sort
from insertion_sort import insertion_sort
from time import perf_counter
from random import randint
import sys


# Generate a list of random integers.
huge_list = []
for x in range(15000):
    huge_list.append(randint(1, 100))


I = huge_list
Q = huge_list


# Insertion Sort
start_time = perf_counter()
insertion_sort(I)
end_time = perf_counter()
time_for_insertion_sort = end_time - start_time


# Manually update recursion limit.
sys.setrecursionlimit(15001)


# Quick Sort
start_time = perf_counter()
quick_sort(Q)
end_time = perf_counter()
time_for_quick_sort = end_time - start_time


print("Insertion Sort = ", time_for_insertion_sort)
print("Quick Sort = ", time_for_quick_sort)
