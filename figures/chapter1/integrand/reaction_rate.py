import numpy as np
import matplotlib.pyplot as plt

from scipy.constants import m_p

m_D = (2 - 0.000994)*m_p
m_T = (3 - 0.006284)*m_p
m_3He = 3.01602932197 * 1.6605438921e-27

eV_to_J = 1.602176634e-19


mu = m_T*m_D / (m_D + m_T)

for species in ["D_T", "D_D", "D_3He"]:

    if species is "D_T":
        mu = m_T*m_D / (m_D + m_T)
    if species is "D_D":
        mu = m_D/2
    if species is "D_3He":
        mu = m_3He*m_D / (m_3He + m_D)

    data = np.loadtxt(f"../cross_section_data/{species}_clean.txt")
    E_keV = data[:, 0]
    E_keV = E_keV[E_keV<1001]
    E_J = E_keV * 1e3 * eV_to_J
    cross_section = data[:, 1][:len(E_J)]

    y = []
    for T in E_J:
        y.append(np.sqrt(8/np.pi) * (mu/T)**(3/2) * 1/(m_D*m_D) * np.trapz(cross_section * E_J * np.exp(-mu/m_D * E_J/T), E_J))

    plt.loglog(E_keV, y)
    plt.xlim(1, 1000)
    plt.ylim(1e-24, 2e-21)

    data = np.column_stack((E_keV, y))
    np.savetxt(f"sigma_v_{species}.txt", data)
    plt.show()
