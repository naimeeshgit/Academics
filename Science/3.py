import random
import numpy as np
from matplotlib import pyplot as plt

N = 100
count = np.zeros(N)
Range = 1000000

for t in range(1,Range):
    d1 = 0
    d2 = 0
    for steps in range(1,N):
        d1 += 2*(random.random()%2) - 1
        d2 += 2*(random.random()%2) - 1

        if(d1 == d2):
            count[steps] += 1

prob = count/Range
print(prob)
# plt.plot(prob)
# plt.show()
        

    
        

