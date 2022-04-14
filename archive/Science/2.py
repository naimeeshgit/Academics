import random
import numpy as np
from matplotlib import pyplot as plt 


list1 = []
list2 = []

for t in range (1,100):
    for i in range(t):
        count = 0
        for i in range(1,100):
            x = random.uniform(-1, 1)
            y= random.uniform(-1, 1)
            if x*x + y*y <= 1:
                count = count + 1

            
        pi = 4*count/100
        list1.append(pi)
        list2.append(t)


plt.plot(list2,list1)
plt.show()
                
            
            
        
        