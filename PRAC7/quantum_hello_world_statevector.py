# quantum_hello_world_statevector.py

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def main():
    # Step 1: Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Step 2: Apply a Hadamard gate to the qubit to create superposition
    qc.h(0)
    
    # Step 3: Generate the statevector from the circuit
    state = Statevector.from_instruction(qc)
    
    # Step 4: Get the probability distribution of outcomes
    probs = state.probabilities_dict()
    print("Statevector probabilities:", probs)
    
    # Step 5: Simulate measurements (1024 times) from the statevector probabilities
    shots = 1024
    outcomes = np.random.choice(list(probs.keys()), size=shots, p=list(probs.values()))
    
    # Step 6: Count how many times each outcome occurred
    unique, counts = np.unique(outcomes, return_counts=True)
    measurement_counts = dict(zip(unique, counts))
    
    # Step 7: Display results
    print("Hello World!")
    print("Simulated measurement counts:", measurement_counts)

if __name__ == "__main__":
    main()
