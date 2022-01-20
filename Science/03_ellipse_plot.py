import numpy as np
from matplotlib import pyplot as plt
from math import pi

u=0.     #x-position of the center
v=0    #y-position of the center
a=4.     #radius on the x-axis
b=3    #radius on the y-axis

t = np.linspace(0, 2*pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
plt.grid(color='lightgray',linestyle='--')
plt.show()