# Variational Quantum Eigensolver (VQE) for H₂ Ground State Energy Simulation

## Overview

This project implements the **Variational Quantum Eigensolver (VQE)** algorithm to estimate the **ground state energy of the Hydrogen molecule (H₂)** using quantum simulation techniques. The implementation combines quantum circuit optimization with classical optimization methods to study how the molecular energy changes with bond length.

The project uses **Qiskit**, **Qiskit Nature**, and **PySCF** to generate the molecular Hamiltonian, map it to qubits, and perform variational optimization.

---

## Project Objectives

- Simulate the ground state energy of the H₂ molecule.
- Construct molecular Hamiltonians for different bond lengths.
- Apply Jordan-Wigner transformation to obtain qubit Hamiltonians.
- Design a parameterized quantum ansatz circuit.
- Optimize variational parameters using COBYLA.
- Generate the molecular potential energy curve.
- Analyze VQE convergence behavior.

---

## Features

- Molecular Hamiltonian generation using PySCF
- Jordan-Wigner fermion-to-qubit mapping
- Custom 4-qubit variational ansatz
- Two-layer parameterized circuit architecture
- COBYLA optimization
- Warm-start parameter initialization
- Energy vs Bond Length analysis
- VQE convergence visualization
- Fully modular code structure

---

## Repository Structure

```text
vqe-h2-ground-state/
│
├── 1.Intro/
│   └── Simulation of Ground State Energy of H.pdf
│
├── 2.code/
│   ├── ansatz.py
│   ├── hamiltonian.py
│   ├── setup.py
│   └── vqe_main.py
│
├── 3.project_results/
│   └── plot_results.py
│
├── 4.outputs/
│   ├── bond_length_comparison.png
│   ├── bond_length_plot.png
│   ├── convergence_plot_new.png
│   └── vqe_energy_plot_new.png
│
├── bond_length_data.json
├── energy_history.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── vqe-env/
│   └── Python virtual environment
│
└── .git/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/namansingh90/vqe-h2-ground-state_final.git
cd vqe-h2-ground-state_final
```

### Create Virtual Environment

```bash
python3 -m venv vqe-env
source vqe-env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Run VQE Simulation

```bash
python 2.code/vqe_main.py
```

This script:

- Generates the H₂ Hamiltonian
- Performs VQE optimization
- Computes energies for multiple bond lengths
- Stores energy values
- Stores optimization history

Generated files:

```text
bond_length_data.json
energy_history.json
```

---

### Step 2: Generate Plots

```bash
python 3.project_results/plot_results.py
```

This generates:

```text
bond_length_comparison.png
bond_length_plot.png
convergence_plot_new.png
vqe_energy_plot_new.png
```

All plots are stored in:

```text
4.outputs/
```

---

## Results

### Energy vs Bond Length Curve

The project computes the ground state energy for bond lengths ranging from:

```text
0.5 Å to 3.5 Å
```

The resulting curve represents the potential energy surface of the Hydrogen molecule.

The minimum point on the curve corresponds to the equilibrium bond length.

---

### Convergence Analysis

The convergence plot shows:

- Optimization iteration number
- Estimated energy value

This demonstrates how the VQE algorithm converges toward the minimum energy solution during optimization.

---

## Implementation Highlights

### Hamiltonian Generation

- PySCF Driver
- STO-3G Basis Set
- Second Quantized Molecular Hamiltonian

### Qubit Mapping

- Jordan-Wigner Transformation

### Quantum Circuit

- 4 Qubits
- 8 Trainable Parameters
- Two RY Rotation Layers
- CNOT Entanglement Layer

### Optimization

- COBYLA Optimizer
- Warm Start Strategy
- Statevector Simulation

---

## Documentation

A complete report containing:

- Quantum Computing Fundamentals
- Variational Quantum Eigensolver Theory
- Hamiltonian Construction
- Ansatz Design
- Workflow Explanation
- Mathematical Background
- Challenges Encountered
- Scalability Discussion
- Future Improvements

is available in:

```text
1.Intro/Simulation of Ground State Energy of H.pdf
```

---

## Technologies Used

- Python
- Qiskit
- Qiskit Nature
- PySCF
- NumPy
- SciPy
- Matplotlib

---

## Future Improvements

Possible extensions of this work include:

- UCCSD Ansatz
- Hardware Execution on IBM Quantum Devices
- Error Mitigation Techniques
- ADAPT-VQE
- Larger Molecules (LiH, BeH₂, H₂O)
- Noise-Aware Simulations
- Quantum Hardware Benchmarking

---

## Authors

**Naman Singh**

Quantum Computing and Quantum Chemistry Simulation Project

---

## License

This project is intended for educational, academic, and research purposes.
