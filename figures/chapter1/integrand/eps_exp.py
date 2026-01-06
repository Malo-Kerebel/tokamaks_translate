import numpy as np
from scipy.constants import m_p

import sys

m_D = (2 - 0.000994)*m_p
m_T = (3 - 0.006284)*m_p

mu = m_T*m_D / (m_D + m_T)

facteur = 1 #.16045250062

data = np.loadtxt("../cross_section_data/D_T_clean.txt")
E = data[:, 0]
E = E[E <= 150] / facteur
cross_section_D_T = data[:, 1][:len(E)]*1e28

x = E/(10/facteur)

y = E * np.exp(-mu/m_D * x)

data = np.column_stack((x, y))
np.savetxt("eps_exp.txt", data)

data = np.column_stack((x, cross_section_D_T))
np.savetxt("sigma.txt", data)

data = np.column_stack((x, y*cross_section_D_T*2))
np.savetxt("integrand.txt", data)

if "--no-show" not in sys.argv:
    import matplotlib.pyplot as plt
    plt.plot(x, y, label="eps_exp")
    plt.plot(x, cross_section_D_T, label="sigma")
    plt.plot(x, y*cross_section_D_T*2, label="integrand")

    plt.legend()
    plt.show()
