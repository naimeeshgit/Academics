from matplotlib import projections
import matplotlib.pyplot as plt
import random as rand
import math

sigma = float(input("input sigma"))
epsilon = float(input("input epsilon"))

x = []
y = []
z = []
points = []
n = 4
min = 0.5
max = 0.6


def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)


while len(points) < n:
    newP = (rand.random(), rand.random(), rand.random())
    check = True

    for p in points:
        if(dist(p, newP) < min or dist(p, newP) > max):
            check = False
            break

    if(check):
        points.append(newP)
        x.append(newP[0])
        y.append(newP[1])
        z.append(newP[2])

U = 0

for p in points:
    for x in points:
        if(x == p):
            continue
        else:
            d = dist(p, x)
            U += 4 * epsilon * ((sigma/d)**12 - (sigma/d)**6)

print(U)