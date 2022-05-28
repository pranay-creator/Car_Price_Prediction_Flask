import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.5)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,Z, rstride=1, cstride=1)
plt.show()