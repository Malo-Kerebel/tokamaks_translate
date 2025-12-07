import numpy as np
import sys


def tau_E(T):
    return 1.5e-15/T


eV_to_J = 1.602176634e-19

E_alpha = 3.5e6 * eV_to_J     # 3.5 MeV en joules

density = 3e20

# Charger les données sigma_v(T)
data = np.loadtxt("../integrand/sigma_v_D_T.txt")
T_keV = data[:, 0]            # T en keV
T_kev = T_keV[T_keV < 30]
sigma_V = data[:, 1][:len(T_keV)]          # <σv> en m^3/s

# Conversion de T en joules
T = T_keV * 1e3 * eV_to_J

# Calcul vectorisé de P_H
P_alpha = 0.25 * density**2 * sigma_V * E_alpha
P_loss = 3 * density * T / tau_E(T)
additional_heating = P_loss - P_alpha

data = np.column_stack((T_keV, P_alpha))
np.savetxt(f"P_alpha_tau_E.txt", data)
data = np.column_stack((T_keV, P_loss))
np.savetxt(f"P_loss_tau_E.txt", data)
data = np.column_stack((T_keV, additional_heating))
np.savetxt(f"P_heating_tau_E.txt", data)


if "--no-show" not in sys.argv:
    import matplotlib.pyplot as plt

    plt.plot(T_keV, P_alpha, label="P_alpha")
    plt.plot(T_keV, P_loss, label="P_loss")
    plt.plot(T_keV, additional_heating, label="additional_heating")
    plt.xlabel("T (keV)")

    plt.xlim(0, 23)
    plt.ylim(0, 1e7)
    plt.legend()
    plt.show()
