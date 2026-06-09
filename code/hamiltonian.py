from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper

def get_h2_hamiltonian(bond_length):
    driver = PySCFDriver(
        atom=f"H 0 0 0; H 0 0 {bond_length}",
        basis="sto3g",
    )

    problem = driver.run()

    second_q_ops = problem.second_q_ops()
    fermionic_hamiltonian = second_q_ops[0]

    #  map to qubit operator
    mapper = JordanWignerMapper()
    qubit_hamiltonian = mapper.map(fermionic_hamiltonian)

    nuclear_repulsion = problem.nuclear_repulsion_energy

    return qubit_hamiltonian, nuclear_repulsion