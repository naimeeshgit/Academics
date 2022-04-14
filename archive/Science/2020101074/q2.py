from matplotlib import projections
import random as rand
import matplotlib.pyplot as plt
import random
import math
from mpl_toolkits import mplot3d
import numpy as np

sigma = float(input("sigma: "))
epsilon = float(input("epsilon: "))


npoints = 4
mindist = 0.5
maxdist = 0.6

x = []
y = []
z = []
points = []

def genpt():
    p_x = random.uniform(0, 1)
    p_y = random.uniform(0, 1)
    p_z = random.uniform(0, 1)
    return(p_x, p_y, p_z)


def distance(p, q):
    dist = (p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2
    dist = math.sqrt(dist)
    return dist



while len(points) < npoints:
    P = genpt()
    flag = 1
    for p in points:
        if(distance(P, p) < mindist or distance(P, p) > maxdist):
            flag = 0
            break
    if(flag == 1):
        points.append(P)
        x.append(P[0])
        y.append(P[1])
        z.append(P[2])


U = 0

for i in points:
    for j in points:
        if(i <= j):
            continue
        else:
            d = distance(i, j)
            U += 4 * epsilon * ((sigma/d)**12 - (sigma/d)**6)

print(U)