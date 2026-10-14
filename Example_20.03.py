import heapq

overview = dir(heapq)
n = len(overview)
counter = 0
for i in range(n):
    if overview[i][0] != "_":
        print("%15s" % overview[i], end="")
        counter += 1
        if counter % 4 == 0:
            print()
