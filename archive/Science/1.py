import random
import numpy as np
from matplotlib import pyplot as plt

list1 = np.zeros()

list2 = np.zeros()
analytical = []

for n in range(0, 100):
    count =0
    for t in range(1, 1000):
        
        xd1 = 0
        xd2 = 0
        for steps in range(1, n+1):

            step1 = random.random()
            step2 = random.random()

            if step1 < 0.5:
                xd1 = xd1-1
            else:
                xd1 = xd1+1

            if step2 < 0.5:
                xd2 = xd2-1
            else:
                xd2 = xd2+1

        if xd1 == xd2:
            count = count + 1

    prob = count/1000
    list1.append(prob)
    list2.append(n)
    analytical.append(1.0/float(n+1))

# plot
plt.plot(list2, list1)
plt.plot(list2, analytical)
plt.show()
