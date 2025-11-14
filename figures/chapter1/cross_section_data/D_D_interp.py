import numpy as np

data = np.loadtxt("D_D.txt")
x = data[:, 0] * 1000
y = data[:, 1] * 1e-28

data = np.loadtxt("D_D_2.txt")
x_2 = data[:, 0] * 1000
y_2 = data[:, 1] * 1e-28

y_2_interp = np.interp(x, x_2, y_2)

data = np.column_stack((x, y+y_2_interp))

np.savetxt("D_D_clean.txt", data)
