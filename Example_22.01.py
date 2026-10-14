from math import inf

def dijkstra(network, start, finish):
    def update_everything(place):
        for pl, dist in net[place]:
            new_total_distance = total_distance[place] + dist
            if total_distance[pl] > new_total_distance:
                total_distance[pl] = new_total_distance
                predecessor[pl] = place
        minimal_distance = inf
        for pl in set_of_all_places:
            if not permanent[pl]:
                if minimal_distance > total_distance[pl]:
                    minimal_distance = total_distance[pl]
                    minimal_distance_place = pl
        permanent[minimal_distance_place] = True
        return minimal_distance_place

    def optimal_path(place):
        pad = []
        pl = place
        while pl != start:
            pad.append(pl)
            pl = predecessor[pl]
        pad.append(start)
        return pad[::-1]

    set_of_all_places = set()
    for pl1, pl2, distance in network:
        set_of_all_places |= {pl1, pl2}
    net = {}
    for pl in set_of_all_places:
        net.setdefault(pl, [])
    for pl1, pl2, distance in network:
        net[pl1].append((pl2, distance))
    total_distance = {}
    permanent = {}
    predecessor = {}
    for place in set_of_all_places:
        total_distance.setdefault(place, inf)
        permanent.setdefault(place, False)
        predecessor.setdefault(place, None)

    place = start
    total_distance[place] = 0
    permanent[place] = True
    predecessor[place] = place
    while not permanent[finish]:
        place = update_everything(place)
    print("The minimal distance from", start, "to", finish,
          "is", total_distance[finish])
    print("The optimal path:", optimal_path(finish))
    print("All available minimal distances and optimal paths:")
    for place in set_of_all_places:
        if permanent[place]:
            print(start, "-->", place, ": %2d"
                  % total_distance[place], optimal_path(place))

network = [
    ("A", "B", 4), ("A", "C", 7), ("A", "D", 5), ("B", "C", 3),
    ("B", "E", 5), ("C", "E", 2), ("C", "F", 6), ("D", "C", 1),
    ("D", "F", 8), ("E", "F", 3), ("E", "G", 6), ("F", "G", 2)
]
dijkstra(network, "A", "G")
