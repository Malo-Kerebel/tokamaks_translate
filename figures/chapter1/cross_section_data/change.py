import numpy as np

for species in ["D_T" "D_3He"]:

    data = np.loadtxt(f"{species}.txt")
    data[:, 0] *= 1000
    data[:, 1] *= 1e-28

    np.savetxt(f"{species}_clean.txt", data)
