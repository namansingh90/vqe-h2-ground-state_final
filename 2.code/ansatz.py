from qiskit import QuantumCircuit

def create_ansatz(params):
    qc = QuantumCircuit(4)

    # Layer 1
    for i in range(4):
        qc.ry(params[i], i)

    # Entanglement
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)

    # Layer 2 (extra expressivity)
    for i in range(4):
        qc.ry(params[i + 4], i)

    return qc



from qiskit import QuantumCircuit
import numpy as np

params = np.zeros(8)  # example parameters

qc = create_ansatz(params)
print(qc.draw())