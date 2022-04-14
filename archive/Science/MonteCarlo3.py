import random
import math

import matplotlib.pyplot as plt


sigma = 4
mu = 0
pi = 3.14159

nhit = 0
ntotal = 0

x = []
y = []


ysigma = 1/(sigma*math.sqrt(2*pi))*math.exp(-0.5*(sigma)**2/sigma**2)

for i in range(10000):
    rx = random.uniform(-2*sigma*sigma, 2*sigma*sigma)
    ry = random.uniform(0, 1)
    if ry <= (1/(sigma*math.sqrt(2*pi)))*math.exp(-0.5*(rx)**2/sigma**2):
        nhit += 1
    ntotal += 1
    x.append(ntotal)
    y.append((nhit/ntotal)*4*sigma*sigma)

plt.plot(x, y)
plt.show()