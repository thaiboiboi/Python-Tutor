from heapq import *

# Start with a regular list:
lst = [7, 2, 5, 8, 10, 4, 6, 1, 3, 9]
# Convert the list to a binary heap and print the result:
heapify(lst)
print(lst)
# Add 6 to the binary heap and print the result:
heappush(lst, 6)
print(lst)
# Remove smallest element from binary heap and print the result:
smallest_element = heappop(lst)
print(lst)
print("The smallest element is", smallest_element)
# Add 7 to heap, then remove smallest element. Print the result:
smallest_element = heappushpop(lst, 7)
print(lst)
print("The smallest element is", smallest_element)
# Delete the smallest element and then add 7. Print the result:
smallest_element = heapreplace(lst, 7)
print(lst)
print("The smallest element is", smallest_element)
# Introduce two sorted lists:
lst1 = [1, 2, 4, 5, 6]
lst2 = [3, 7, 8, 9, 10]
# Merge the two sorted lists into a sorted list and print the
# result:
lst_merged = list(merge(lst1, lst2))
print(lst_merged)
# Find the 3 largest numbers in the following list and print
# the result:
lst = [7, 2, 5, 8, 10, 4, 6, 1, 3, 9]
print("The 3 largest numbers are:", nlargest(3, lst))
# Find the 4 smallest numbers in the following list and print
# the result:
lst = [7, 2, 5, 8, 10, 4, 6, 1, 3, 9]
print("The 4 smallest numbers are:", nsmallest(4, lst))
