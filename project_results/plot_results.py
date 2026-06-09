import json
import numpy as np
import matplotlib.pyplot as plt


# LOADING DATA

with open("bond_length_data.json", "r") as f:
    data = json.load(f)

bond_lengths = np.array(data["bond_lengths"])
energies = np.array(data["energies"])


# SORTING DATA (important for interpolation)

sorted_indices = np.argsort(bond_lengths)
bond_lengths = bond_lengths[sorted_indices]
energies = energies[sorted_indices]


# FINDING MINIMUM

min_index = np.argmin(energies)
min_energy = energies[min_index]
min_bond = bond_lengths[min_index]

print("Minimum Energy:", min_energy)
print("At Bond Length:", min_bond)


# SAFE SMOOTHING (NO OVERFITTING)

x_smooth = np.linspace(bond_lengths.min(), bond_lengths.max(), 300)
y_smooth = np.interp(x_smooth, bond_lengths, energies)  


# PLOTING: ENERGY CURVE

plt.figure(figsize=(10, 6))

# Raw data points
plt.plot(bond_lengths, energies, 'o', label="VQE Data")

# Interpolated curve (safe)
plt.plot(x_smooth, y_smooth, '-', label="VQE Curve")

# Mark minimum
plt.scatter(min_bond, min_energy)
plt.annotate(f"Min ({min_bond:.2f}, {min_energy:.3f})",
             (min_bond, min_energy),
             textcoords="offset points",
             xytext=(10, -15))

# Labels
plt.xlabel("Bond Length (Å)")
plt.ylabel("Energy (Hartree)")
plt.title("H₂ Ground State Energy (VQE)")
plt.legend()
plt.grid()

# Save plot
plt.savefig("vqe_energy_plot_new.png", dpi=300)
plt.close()


# CONVERGENCE PLOTING

try:
    with open("energy_history.json", "r") as f:
        energy_history = json.load(f)

    plt.figure(figsize=(7, 4))
    plt.plot(energy_history, marker='o')

    plt.xlabel("Iteration")
    plt.ylabel("Energy (Hartree)")
    plt.title("VQE Convergence")
    plt.grid()

    plt.savefig("convergence_plot_new.png", dpi=300)
    plt.close()

except FileNotFoundError:
    print("No convergence data found")