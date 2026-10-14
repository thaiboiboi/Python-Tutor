from heapq import *
from random import *
from time import time

def heap_sort(lst):
    heapify(lst)
    lst_sorted = []
    n = len(lst)
    for i in range(n):
        lst_sorted.append(heappop(lst))
    return lst_sorted

# Create a list with n random numbers:
n = 1000000
lst = [random() for i in range(n)]
# Sort the list using heap_sort and time this operation:
t1 = time()
lst_sorted = heap_sort(lst)
t2 = time()
t = t2 - t1
print("Sorting takes %.3f seconds" % t)
