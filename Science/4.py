import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
# plt.plot(x,y)
# plt.show()
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()
# x = np.arange(0,4*np.pi-1,0.1)   # start,stop,step
# y = np.sin(x)
# z = np.cos(x)