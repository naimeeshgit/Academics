import random
import numpy as np
np.random.seed(100)

x1 = random.uniform(0,10)
y1 = random.uniform(0,10)
z1 = random.uniform(0,10)

x2 = random.uniform(0,10)
y2 = random.uniform(0,10)
z2 = random.uniform(0,10)

var1 = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
while var1 < 25 or var1 > 36:
    x2 = random.uniform(0,10)
    y2 = random.uniform(0,10)
    z2 = random.uniform(0,10)
    var1 = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))

x3 = random.uniform(0,10)
y3 = random.uniform(0,10)
z3 = random.uniform(0,10)

var2 = ((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)+(z1-z3)*(z1-z3))
var3 = ((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)+(z2-z3)*(z2-z3))
while var2 < 25 or var2 > 36 or var3 < 25 or var3 > 36:
    x3 = random.uniform(0,10)
    y3 = random.uniform(0,10)
    z3 = random.uniform(0,10)
    var2 = ((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)+(z1-z3)*(z1-z3))
    var3 = ((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)+(z2-z3)*(z2-z3))

x4 = random.uniform(0,10)
y4 = random.uniform(0,10)
z4 = random.uniform(0,10)

var4 = ((x1-x4)*(x1-x4)+(y1-y4)*(y1-y4)+(z1-z4)*(z1-z4))
var5 = ((x2-x4)*(x2-x4)+(y2-y4)*(y2-y4)+(z2-z4)*(z2-z4))
var6 = ((x3-x4)*(x3-x4)+(y3-y4)*(y3-y4)+(z3-z4)*(z3-z4))
while var4 < 25 or var4 > 36 or var5 < 25 or var5 > 36 or var6 < 25 or var6 > 36:
    x4 = random.uniform(0,10)
    y4 = random.uniform(0,10)
    z4 = random.uniform(0,10)
    var4 = ((x1-x4)*(x1-x4)+(y1-y4)*(y1-y4)+(z1-z4)*(z1-z4))
    var5 = ((x2-x4)*(x2-x4)+(y2-y4)*(y2-y4)+(z2-z4)*(z2-z4))
    var6 = ((x3-x4)*(x3-x4)+(y3-y4)*(y3-y4)+(z3-z4)*(z3-z4))

print("distance between point 1 and 2 is", np.sqrt(var1))
print("distance between point 1 and 3 is", np.sqrt(var2))
print("distance between point 2 and 3 is", np.sqrt(var3))
print("distance between point 1 and 4 is", np.sqrt(var4))
print("distance between point 2 and 4 is", np.sqrt(var5))
print("distance between point 3 and 4 is", np.sqrt(var6))

print("x,y,z of point 1 are ", x1, y1, z1)
print("x,y,z of point 2 are ",x2, y2, z2)
print("x,y,z of point 3 are ",x3, y3, z3)
print("x,y,z of point 4 are ",x4, y4, z4)

epsilon = float(input("Enter epsilon value"))
sigma = float(input("Enter sigma value"))

print("Interaction energy b/w between point 1 and 2 is", 4*epsilon*( (sigma/np.sqrt(var1))**12 - (sigma/np.sqrt(var1))**6 ))
print("Interaction energy b/w between point 1 and 3 is", 4*epsilon*( (sigma/np.sqrt(var2))**12 - (sigma/np.sqrt(var2))**6 ))
print("Interaction energy b/w between point 2 and 3 is", 4*epsilon*( (sigma/np.sqrt(var3))**12 - (sigma/np.sqrt(var3))**6 ))
print("Interaction energy b/w between point 1 and 4 is", 4*epsilon*( (sigma/np.sqrt(var4))**12 - (sigma/np.sqrt(var4))**6 ))
print("Interaction energy b/w between point 2 and 4 is", 4*epsilon*( (sigma/np.sqrt(var5))**12 - (sigma/np.sqrt(var5))**6 ))
print("Interaction energy b/w between point 3 and 4 is", 4*epsilon*( (sigma/np.sqrt(var6))**12 - (sigma/np.sqrt(var6))**6 ))

"""
        r (float): Atom-atom distance (Angstrom).
        A (float): Interaction parameter (eV Angstrom^12).
        B (float): Interaction parameter (eV Angstrom^6).
"""

def first_derivative(r, A, B):

    return -12. * A / r ** 13 + 6 * B / r ** 7

A = 1e5
B = 40

alpha = 100
r = np.sqrt(var1)
r_list = [r]
for i in range(30):
    E_dash = first_derivative(r, A, B)
    r = r - alpha * E_dash
    r_list.append(r)

import matplotlib.pyplot as plt

plt.plot(range(31), r_list, 'o--')
plt.xlabel('Iteration')
plt.ylabel('r')
plt.title("Interaction energy b/w between point 1 and 2")
plt.show()

r = np.sqrt(var2)
r_list = [r]
for i in range(30):
    E_dash = first_derivative(r, A, B)
    r = r - alpha * E_dash
    r_list.append(r)

plt.plot(range(31), r_list, 'o--')
plt.xlabel('Iteration')
plt.ylabel('r')
plt.title("Interaction energy b/w between point 1 and 3")
plt.show()

r = np.sqrt(var3)
r_list = [r]
for i in range(30):
    E_dash = first_derivative(r, A, B)
    r = r - alpha * E_dash
    r_list.append(r)

plt.plot(range(31), r_list, 'o--')
plt.xlabel('Iteration')
plt.ylabel('r')
plt.title("Interaction energy b/w between point 2 and 3")
plt.show()

r = np.sqrt(var4)
r_list = [r]
for i in range(30):
    E_dash = first_derivative(r, A, B)
    r = r - alpha * E_dash
    r_list.append(r)

plt.plot(range(31), r_list, 'o--')
plt.xlabel('Iteration')
plt.ylabel('r')
plt.title("Interaction energy b/w between point 1 and 4")
plt.show()

r = np.sqrt(var5)
r_list = [r]
for i in range(30):
    E_dash = first_derivative(r, A, B)
    r = r - alpha * E_dash
    r_list.append(r)

plt.plot(range(31), r_list, 'o--')
plt.xlabel('Iteration')
plt.ylabel('r')
plt.title("Interaction energy b/w between point 2 and 4")
plt.show()

r = np.sqrt(var6)
r_list = [r]
for i in range(30):
    E_dash = first_derivative(r, A, B)
    r = r - alpha * E_dash
    r_list.append(r)

plt.plot(range(31), r_list, 'o--')
plt.xlabel('Iteration')
plt.ylabel('r')
plt.title("Interaction energy b/w between point 3 and 4")
plt.show()