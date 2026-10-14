# The function merge combines two ordered lists to a single list. 
# This version prints intermediate steps to clarify its functioning:
def merge(lst1, lst2):
    # Function that prints intermediate output:
    def print_output(t1plus, t2plus):
        global counter
        print("  Step %d:" % counter)
        print("List 1:", lst1)
        print("List 2:", lst2)
        if t1plus:
            print("Counter 1:", counter1, "->", counter1 + 1)
        else:
            print("Counter 1:", counter1)
        if t2plus:
            print("Counter 2:", counter2, "->", counter2 + 1)
        else:
            print("Counter 2:", counter2)
        print("Merged list:", lst_merge)
        counter += 1

    counter1 = 0
    counter2 = 0
    n1 = len(lst1)
    n2 = len(lst2)
    lst_merge = []
    print_output(False, False)
    while (counter1 < n1) and (counter2 < n2):
        if lst1[counter1] < lst2[counter2]:
            lst_merge.append(lst1[counter1])
            print_output(True, False)
            counter1 += 1
        else:
            lst_merge.append(lst2[counter2])
            print_output(False, True)
            counter2 += 1
    while counter1 < n1:
        lst_merge.append(lst1[counter1])
        print_output(True, False)
        counter1 += 1
    while counter2 < n2:
        lst_merge.append(lst2[counter2])
        print_output(False, True)
        counter2 += 1
    return lst_merge

counter = 0
# Two ordered lists:
list1 = [2, 5, 7, 8, 10]
list2 = [1, 3, 4, 6, 9]
# Merge both lists and print intermediate output:
list_merged = merge(list1, list2)
