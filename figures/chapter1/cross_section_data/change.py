import numpy as np

data = np.loadtxt("D_3He.txt")
data[:, 0] *= 1000
data[:, 1] *= 1e-28

np.savetxt("D_3He.txt", data)
