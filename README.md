# Variational Quantum Eigensolver (VQE) for H₂ Ground State Energy

A quantum computing project that uses the Variational Quantum Eigensolver (VQE) algorithm to estimate the ground state energy of the Hydrogen (H₂) molecule across different bond lengths.

The project is implemented using Qiskit, Qiskit Nature, PySCF, NumPy, SciPy, and Matplotlib.

## Features

- Generation of molecular Hamiltonian using PySCF
- Jordan-Wigner mapping from fermionic to qubit operators
- Custom 4-qubit parameterized ansatz
- COBYLA-based variational optimization
- Warm-start optimization for faster convergence
- Ground state energy estimation across multiple bond lengths
- Energy vs Bond Length visualization
- VQE convergence analysis

## Repository Structure

```
vqe-h2-ground-state_final/
│
├── code/
│   ├── ansatz.py
│   ├── hamiltonian.py
│   ├── setup.py
│   └── vqe_main.py
│
├── outputs/
│   ├── bond_length_comparison.png
│   ├── bond_length_plot.png
│   ├── convergence_plot_new.png
│   └── vqe_energy_plot_new.png
│
├── project_results/
│   └── plot_results.py
│
├── Intro/
│   └── Simulation of Ground State Energy of H.pdf
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/namansingh90/vqe-h2-ground-state_final.git
cd vqe-h2-ground-state_final
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Execute the main VQE simulation:

```bash
python code/vqe_main.py
```

This will:

- Generate the H₂ molecular Hamiltonian
- Run VQE optimization for different bond lengths
- Store energy values
- Save convergence history

Generate plots:

```bash
python project_results/plot_results.py
```

## Outputs

The project generates:

### Energy vs Bond Length Curve

Shows how the molecular ground state energy varies with internuclear separation and identifies the equilibrium bond length.

### Convergence Plot

Shows the optimization trajectory of the VQE algorithm and demonstrates convergence toward the minimum energy solution.

All generated plots can be found in the `outputs/` directory.

## Documentation

A detailed explanation of the theory, implementation, workflow, challenges, and future scope is available in:

```
Intro/Simulation of Ground State Energy of H.pdf
```

## Technologies Used

- Python
- Qiskit
- Qiskit Nature
- PySCF
- NumPy
- SciPy
- Matplotlib

## Authors

- Naman Singh
- Project Team Members

## License

This project is intended for educational and research purposes.
