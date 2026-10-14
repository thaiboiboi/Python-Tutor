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

# Define list with n arbitrary numbers:
lst = [7, 2, 5, 8, 10, 4, 6, 1, 3, 9]
# Print the original list:
print("Original list:", lst)
# Apply merge_sort and print the final result:
list_sorted = merge_sort(lst)
print("Ordered list: ", list_sorted)
