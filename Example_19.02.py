# The function insertion_sort with intermediate steps:
def insertion_sort(lst):
    n = len(lst)
    counter = 0
    for i in range(n):
        for j in range(i):
            if lst[i - j] < lst[i - j - 1]:
                counter += 1
                lst[i - j], lst[i - j - 1] = lst[i - j - 1], lst[i - j]
                print("Step %2d:" % counter, lst)
            else:
                break
    return lst

def sort(lst):
    n = len(lst)
    counter = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                counter +=1
                print("Step %2d:" % counter, lst)
    return lst

# Define list with n arbitrary numbers:
lst = [7, 2, 5, 8, 10, 4, 6, 1, 3, 9]
# Print the original list:
print("Step  0:", lst)
# Apply insertion_sort and print the intermediate steps:
list_sorted = insertion_sort(lst)
print()
list_sorted = sort(lst)
