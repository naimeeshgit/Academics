import random
import math

import matplotlib.pyplot as plt


x = []
y = []

nhit = 0
ntotal = 0

for i in range(1000):
    rx = random.uniform(0, 1)
    ry = random.uniform(0, 1)
    rz = random.uniform(0, 1)
    if ry*rx**2 >= rz:
        nhit += 1
    ntotal += 1
    x.append(ntotal)
    y.append((nhit/ntotal))

plt.plot(x, y)
plt.show()