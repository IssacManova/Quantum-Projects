from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create circuit
n_qubits = 3
qc = QuantumCircuit(n_qubits, n_qubits)

# Example input state |101>
qc.x(0)
qc.x(2)

# Apply Quantum Fourier Transform
qft = QFT(num_qubits=n_qubits)
qc.append(qft, range(n_qubits))

# Measure
qc.measure(range(n_qubits), range(n_qubits))

# Run simulation
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()
counts = result.get_counts()

print("QFT Output:")
print(counts)

plot_histogram(counts)
plt.show()