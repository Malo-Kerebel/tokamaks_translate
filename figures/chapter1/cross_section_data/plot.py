import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("D_3He_clean.txt")

x = data[:, 0]
y = data[:, 1]

plt.loglog(x, y)

data = np.loadtxt("D_D_clean.txt")

x = data[:, 0]
y = data[:, 1]
plt.loglog(x, y)

data = np.loadtxt("D_D_2.txt")

x = data[:, 0]
y = data[:, 1]
plt.loglog(x, y)

data = np.loadtxt("D_T_clean.txt")

x = data[:, 0]
y = data[:, 1]
plt.loglog(x, y)
plt.xlim(1, 1000)
plt.ylim(1e-32, 1e-26)
plt.show()
