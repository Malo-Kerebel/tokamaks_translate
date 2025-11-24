import numpy as np

import matplotlib.pyplot as plt

eV_to_J = 1.602176634e-19

E_keV = np.linspace(0.5, 2000, 10000)
E_J = E_keV

E_G = 31.3970
A_1 = 5.5576e4
A_2 = 2.1054e2
A_3 = -3.2638e-2
A_4 = 1.4987e-6
A_5 = 1.8181e-10
B_1 = 0
B_2 = 0
B_3 = 0
B_4 = 0


y = A_1 + E_J * (A_2 + E_J * (A_3 + E_J * (A_4 + E_J * A_5)))
y *= 1 + E_J * (B_1 + E_J * (B_2 + E_J * (B_3 + E_J * B_4)))

plt.loglog(E_keV, y/(E_J * np.exp(E_G/ np.sqrt(E_J))))

plt.show()
