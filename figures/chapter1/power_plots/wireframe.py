from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

eV_to_J = 1.602176634e-19

E_alpha = 3.5e6 * eV_to_J     # 3.5 MeV en joules
tau_E = 0.5                     # temps de confinement en s

N = 100
density = np.linspace(3e19, 3e20, N)

# Charger les données sigma_v(T)
data = np.loadtxt("../integrand/sigma_v_D_T.txt")
T_keV = data[:, 0]            # T en keV
T_keV = T_keV[T_keV < 44]
sigma_V = data[:, 1][:len(T_keV)]          # <σv> en m^3/s

print(len(T_keV), len(T_keV) * N)

# Conversion de T en joules
T = T_keV * 1e3 * eV_to_J

# Meshgrid
Density, Temp = np.meshgrid(density, T)

# Calcul vectorisé de P_H
P = 3 * Density * Temp / tau_E - 0.25 * Density**2 * sigma_V[:, None] * E_alpha

seuil_max = 4e6
seuil_min = 0
# P = np.clip(P, seuil_min, seuil_max)

# Tracé
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_wireframe(Temp / (1e3 * eV_to_J) / 2, Density, P)

ax.set_xlim(0, 22)
ax.set_zlim(seuil_min, seuil_max)

ax.set_xlabel('T (keV)')
ax.set_ylabel('n (m^-3)')
ax.set_zlabel('P_H (W/m^3)')

# Export wireframe data for pgfplots: columns = T_keV, density, P
wireframe_data = np.column_stack([
    Temp.flatten() / (1e3 * eV_to_J),   # T en keV
    Density.flatten(),                  # n en m^-3
    P.flatten()                         # P_H
])

np.savetxt("wireframe_data.txt", wireframe_data, fmt="%.5e")


plt.show()

plt.contour(Temp / (1e3 * eV_to_J), Density, P, levels=30)
plt.colorbar(label="P_H (W/m³)")
plt.xlabel("T (keV)")
plt.ylabel("n (m⁻³)")

plt.yscale("log")

plt.show()
