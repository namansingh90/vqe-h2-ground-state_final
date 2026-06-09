import numpy as np
from scipy.optimize import minimize
import json

from qiskit.quantum_info import Statevector

from hamiltonian import get_h2_hamiltonian
from ansatz import create_ansatz


# GLOBAL VARIABLES

current_hamiltonian = None
energy_history = []


# ENERGY FUNCTION

def compute_energy(params, hamiltonian):
    circuit = create_ansatz(params)
    statevector = Statevector.from_instruction(circuit)

    energy = np.real(statevector.expectation_value(hamiltonian.to_matrix()))
    return energy


# CALLBACK (for convergence plot)

def callback(xk):
    global current_hamiltonian
    energy = compute_energy(xk, current_hamiltonian)
    energy_history.append(energy)
    print(f"Iter Energy: {energy:.6f}")


# BOND LENGTH EXPERIMENT

bond_lengths = np.linspace(0.5, 3.5, 30)
energies = []

params = np.zeros(8)   

for r in bond_lengths:
    print(f"\nRunning for bond length = {r:.2f}")

    hamiltonian, nuclear_repulsion = get_h2_hamiltonian(r)

    current_hamiltonian = hamiltonian
    energy_history.clear()

    result = minimize(
        lambda p: compute_energy(p, hamiltonian),
        params,                      # warm start
        method='COBYLA',
        callback=callback,
        options={'maxiter': 200}
    )

    params = result.x  

    vqe_energy = result.fun

    total_energy = vqe_energy + nuclear_repulsion

    energies.append(total_energy)

    print(f"Electronic Energy: {vqe_energy:.6f}")
    print(f"Total Energy: {total_energy:.6f}")


# SAVING ENERGY CURVE

with open("bond_length_data.json", "w") as f:
    json.dump({
        "bond_lengths": bond_lengths.tolist(),
        "energies": energies
    }, f)


# SAVEING LAST CONVERGENCE

with open("energy_history.json", "w") as f:
    json.dump(energy_history, f)

print("\nAll energies:", energies)