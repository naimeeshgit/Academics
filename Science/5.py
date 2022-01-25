import matplotlib.pyplot as plt
import random
import math
from mpl_toolkits import mplot3d
import numpy as np

npoints = 4
mindist = 0.5
maxdist = 0.6

def genpt():
    return (random.random(), random.random(), random.random())

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

xpt = []
ypt = []
zpt = []
points = []

while len(points) < npoints:
    newpt = genpt()
    flag = 1
    for p in points:
        if(distance(newpt, p) < mindist or distance(newpt, p) > maxdist):
            flag = 0
            break
    if(flag == 1):
        points.append(newpt)
        xpt.append(newpt[0])
        ypt.append(newpt[1])
        zpt.append(newpt[2])

print(points)

ax = plt.axes(projection ="3d")

ax.scatter3D(xpt, ypt, zpt, color = "blue")
 
plt.show()