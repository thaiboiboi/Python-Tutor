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

# Compute the total distance of a route using the distance matrix:
def total_dist(route, dist_mat):
    n = len(route)
    total = 0
    for i in range(n - 1):
        total += dist_mat[route[i] - 1][route[i + 1] - 1]
    return total

# Serial numbers of the available cities:
lst = [1, 2, 3, 4]
# Serial number of the start:
start = 1
# Serial number of the finish:
end = 1
# Distance matrix containing the distances between the cities:
dist = [
    [0, 6, 10, 2],
    [6, 0, 3, 4],
    [10, 3, 0, 15],
    [2, 4, 15, 0]
]
# Find all routes with given start and finish:
list_all_routes = all_routes(lst, start, end)
# Determine the total distance of all these routes:
list_tot_dist = []
for route in list_all_routes:
    list_tot_dist.append(total_dist(route, dist))
# Print the routes and corresponding total distances:
n_routes = len(list_all_routes)
for i in range(n_routes):
    route = list_all_routes[i]
    print("%3d:" % (i + 1), route, "%3d" % list_tot_dist[i])
# Determine the minimum total distance and the corresponding
# indices in the list of all routes:
min_dist = 1000000
list_min_dist = []
for i in range(n_routes):
    route = list_all_routes[i]
    dist_route = total_dist(route, dist)
    if dist_route < min_dist:
        min_dist = dist_route
        list_min_dist = [route]
    elif dist_route == min_dist:
        list_min_dist.append(route)
print("Routes with the shortest distance are:")
for route in list_min_dist:
    print(route)
print("These routes have the shortest distance", min_dist)
