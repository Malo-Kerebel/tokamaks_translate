import numpy as np
import matplotlib.pyplot as plt

eV_to_J = 1.602176634e-19

data = np.loadtxt("../integrand/sigma_v_D_T.txt")
T_keV = data[:, 0]      # T en keV
sigma_v = data[:, 1]    # <σv> en m^3/s
T_J = T_keV * 1e3 * eV_to_J

dsig_dT = np.gradient(sigma_v, T_J)

stab_condition = 1 - (T_J / sigma_v) * dsig_dT

plt.plot(T_keV, stab_condition)
plt.xlim(0, 37)
plt.ylim(-2, 1)
plt.show()

data = np.column_stack((T_keV, stab_condition))
np.savetxt(f"stability_condition.txt", data)
