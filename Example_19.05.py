from random import *
from time import time

# The function insertion_sort:
def insertion_sort(lst):
    n = len(lst)
    counter = 0
    for i in range(n):
        for j in range(i):
            if lst[i - j] < lst[i - j - 1]:
                counter += 1
                lst[i - j], lst[i - j - 1] = lst[i - j - 1], lst[i - j]
            else:
                break
    return lst

# The function merge combines two ordered lists to a single list:
def merge(lst1, lst2):
    counter1 = 0
    counter2 = 0
    n1 = len(lst1)
    n2 = len(lst2)
    lst_merge = []
    while (counter1 < n1) and (counter2 < n2):
        if lst1[counter1] < lst2[counter2]:
            lst_merge.append(lst1[counter1])
            counter1 += 1
        else:
            lst_merge.append(lst2[counter2])
            counter2 += 1
    while counter1 < n1:
        lst_merge.append(lst1[counter1])
        counter1 += 1
    while counter2 < n2:
        lst_merge.append(lst2[counter2])
        counter2 += 1
    return lst_merge

# The function merge_sort sorts a list via merge sort:
def merge_sort(lst):
    n = len(lst)
    if n > 1:
        center = n // 2
        lst_left = merge_sort(lst[:center])
        lst_right = merge_sort(lst[center:])
        return merge(lst_left, lst_right)
    else:
        return lst

# Create a list with n random numbers:
n = 10000
lst = [random() for i in range(n)]
# Create two copies to sort:
lst1 = lst[:]
lst2 = lst[:]
# Sort lst1 with insertion sort and time this operation:
t1 = time()
lst1_sorted = insertion_sort(lst1)
t2 = time()
t = t2 - t1
print("Insertion sort is executed in %.2f seconds" % t)
# Sort lst2 with merge sort and time the operation:
t1 = time()
lst2_sorted = merge_sort(lst2)
t2 = time()
t = t2 - t1
print("Merge sort is executed in %.2f seconds" % t)
