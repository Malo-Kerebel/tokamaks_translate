import numpy as np
import sys

eV_to_J = 1.602176634e-19

# Charger les données sigma_v(T)
data = np.loadtxt("../integrand/sigma_v_D_T.txt")
T_keV = data[:, 0]            # T en keV
T = T_keV * 1e3 * eV_to_J
sigma_V = data[:, 1][:len(T_keV)]          # <σv> en m^3/s

E_alpha = 3.5 * 1e6 * eV_to_J

y = 12/sigma_V * T / E_alpha

data = np.column_stack((T_keV, y))
np.savetxt(f"n_tau_E_ignition.txt", data)

if "--no-show" not in sys.argv:
    import matplotlib.pyplot as plt

    plt.loglog(T_keV, y)
    plt.xlim(3, 300)
    plt.ylim(1e20, 1e22)

    plt.show()
