# VQE for H₂ Molecule Ground State

##  Overview

This project implements the Variational Quantum Eigensolver (VQE) algorithm to compute the ground state energy of the hydrogen (H₂) molecule using a hybrid quantum-classical approach.

---

##  Objective

* Compute ground state energy of H₂ molecule
* Use a parameterized quantum circuit (ansatz)
* Optimize using a classical optimizer
* Evaluate energy at different bond lengths

---

##  Project Structure

```
vqe-h2-ground-state/
│── code/
│   ├── ansatz.py
│   ├── hamiltonian.py
│   ├── setup.py
│   ├── vqe_main.py
│
│── report/
│── presentation/
│── project_results/
│── bond_length_data.json
│── requirements.txt
│── README.md
```

---

##  Installation

```bash
git clone <repo-url>
cd vqe-h2-ground-state
pip install -r requirements.txt
```

---

##  Run the Project

```bash
python code/vqe_main.py
```

---

##  Output
pictures:
* Ground state energy of H₂
* Results for different bond lengths

---

##  Requirements

* qiskit
* numpy
* scipy
* matplotlib (if used)

Install using:

```bash
pip install -r requirements.txt
```


---

##  Note

This is an academic project implementing basic VQE for learning purposes.
