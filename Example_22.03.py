# Append every list in a given list with a certain element to 
# the left:
def add_element(lst, element):
    lst_added = []
    for el in lst:
        lst_added.append([element] + el)
    return lst_added

# Append every list in a given list with the given elements to 
# the left and to the right:
def add_two_sides(lst, element_left, element_right):
    lst_added = []
    for el in lst:
        lst_added.append([element_left] + el + [element_right])
    return lst_added

# Determine the list with all possible permutations of a given
# list
def all_permutations(lst):
    n = len(lst)
    if n == 0:
        return [[]]
    else:
        list_all_permutations = []
        for i in range(n):
            lst_reduced = all_permutations(lst[:i] + lst[i + 1:])
            list_inc = add_element(lst_reduced, lst[i])
            list_all_permutations += list_inc
        return list_all_permutations

# Determine a list with all possible routes from start to end
# passing all locations provided in a given list:
def all_routes(lst, start, end):
    list_intermediate = list(set(lst) - {start, end})
    list_all_perm = all_permutations(list_intermediate)
    list_routes = add_two_sides(list_all_perm, start, end)
    return list_routes

# Serial numbers of the available cities:
lst = [1, 2, 3, 4]
# Serial number of the start:
start = 1
# Serial number of the finish:
end = 1
# Find all routes with given start and finish and print these:
list_all_routes = all_routes(lst, start, end)
counter = 0
for route in list_all_routes:
    counter += 1
    print("%3d:" % counter, route)
