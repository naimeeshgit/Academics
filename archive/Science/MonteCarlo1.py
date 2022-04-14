import random
import math

import matplotlib.pyplot as plt

nhit = 0
ntotal = 0

x = []
y = []

for i in range(1000):
    rx = random.uniform(0, 1)
    ry = random.uniform(0, 3)
    if 3*rx**2 >= ry:
        nhit += 1
    ntotal += 1
    x.append(ntotal)
    y.append((3*nhit/ntotal))

plt.plot(x, y)
plt.show()