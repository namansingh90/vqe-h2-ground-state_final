# this file is only to test whether qiskit libraries are there or not 
# it has no major use in the project

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

# Create simple circuit
qc = QuantumCircuit(1)
qc.h(0)

# Simulator
sim = Aer.get_backend('aer_simulator')

# Transpile + run
qc = transpile(qc, sim)
result = sim.run(qc).result()

print("Qiskit working perfectly ")