from random import *
from time import time

import matplotlib.pyplot as plt

# Create a list with n random numbers:
n = 1000000
lst = [random() for i in range(n)]
# Determine the size by which the length of sub-lists are increased:
n_increase = 10000
# Initialize two lists to store list sizes and time:
list_size = []
list_time = []
# Loop that times how long it takes to compute the lists of 
# averages of lists of increasing size:
for i in range(n // n_increase):
    size = n_increase * (i + 1)
    sub_list = lst[:size]
    t1 = time()
    sub_list.sort()
    t2 = time()
    t = t2 - t1
    list_size.append(size)
    list_time.append(t)
# Plot the timing results:
plt.plot(list_size, list_time, color="red", linestyle="solid",
         linewidth=1)
plt.grid(True)
plt.xlabel("List size")
plt.ylabel("Time")
plt.show()
