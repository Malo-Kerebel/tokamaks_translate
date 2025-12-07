import numpy as np
import sys

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

with open("data_matrix.dat", "w") as f:
    for j in range(0, len(density), 2):
        for i in range(0, len(T), 2):
            f.write(f"{T_keV[i]:.6f} {density[j]:.6f} {P[i, j]:.6f}\n")
        f.write("\n")  # ligne vide à la fin de chaque rangée

# Tracé
if "--no-show" not in sys.argv:
    from mpl_toolkits import mplot3d
    import sys

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_wireframe(Temp / (1e3 * eV_to_J) / 2, Density, P)

    ax.set_xlim(0, 22)
    ax.set_zlim(seuil_min, seuil_max)

    ax.set_xlabel('T (keV)')
    ax.set_ylabel('n (m^-3)')
    ax.set_zlabel('P_H (W/m^3)')

    plt.show()

    plt.contour(Temp / (1e3 * eV_to_J), Density, P, levels=30)
    plt.colorbar(label="P_H (W/m³)")
    plt.xlabel("T (keV)")
    plt.ylabel("n (m⁻³)")

    plt.yscale("log")

    plt.show()
