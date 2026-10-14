from heapq import *

def prim(network, start):
    net = {}
    set_connected = set()
    set_not_connected = set()
    for pl1, pl2, length in network:
        net.setdefault(pl1, []).append((pl2, length))
        net.setdefault(pl2, []).append((pl1, length))
        set_not_connected.add(pl1)
        set_not_connected.add(pl2)
    path = []
    total_length = 0
    place = start
    set_connected |= {place}
    set_not_connected -= {place}
    while set_not_connected != set():
        binary_heap = []
        for pl1 in set_connected:
            for pl2, length in net[pl1]:
                if pl2 in set_not_connected:
                    heappush(binary_heap, (length, pl1, pl2))
        minimum_length, min_pl1, min_pl2 = heappop(binary_heap)
        total_length += minimum_length
        path.append((min_pl1, min_pl2))
        place = min_pl2
        set_connected |= {place}
        set_not_connected -= {place}
    print("The total length of the minimum spanning tree is",
          total_length)
    print("The arcs of the minimum spanning tree are:")
    counter = 0
    for connection in path:
        print(connection, end="  ")
        counter += 1
        if counter % 5 == 0:
            print()
    print()

network = [
    ("A", "B", 30), ("A", "C", 45), ("B", "E", 25),
    ("B", "G", 35), ("B", "H", 50), ("C", "D", 50),
    ("C", "F", 20), ("C", "I", 60), ("D", "F", 45),
    ("E", "F", 40), ("E", "G", 15), ("F", "I", 30),
    ("F", "J", 35), ("G", "H", 30), ("G", "J", 20),
    ("H", "J", 25), ("I", "J", 40)
]

prim(network, "A")
