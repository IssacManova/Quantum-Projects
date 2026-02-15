from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import PhaseGate, QFT
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

# Number of counting qubits
n_count = 3

# Create circuit
qc = QuantumCircuit(n_count + 1, n_count)

# Step 1: Prepare eigenstate |1>
qc.x(n_count)

# Step 2: Apply Hadamard to counting qubits
qc.h(range(n_count))

# Step 3: Controlled unitary operations
angle = 2 * np.pi * 0.125  # phase = 1/8
for i in range(n_count):
    qc.cp(angle * (2**i), i, n_count)

# Step 4: Inverse QFT
qc.append(QFT(n_count, inverse=True), range(n_count))

# Step 5: Measure counting qubits
qc.measure(range(n_count), range(n_count))

# Run simulation
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()
counts = result.get_counts()

print("Phase Estimation Result:")
print(counts)

plot_histogram(counts)
plt.show()
