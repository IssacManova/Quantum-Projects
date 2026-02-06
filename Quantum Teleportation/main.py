from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


print("Program started...")
# Create circuit with 3 qubits and 2 classical bits
qc = QuantumCircuit(3, 2)

# Step 1: Prepare a state to teleport (|1⟩ example)
qc.x(0)

# Step 2: Create entanglement between qubit 1 and 2
qc.h(1)
qc.cx(1, 2)

# Step 3: Bell measurement
qc.cx(0, 1)
qc.h(0)

# Step 4: Measure qubits
qc.measure(0, 0)
qc.measure(1, 1)

# Step 5: Apply corrections
qc.cx(1, 2)
qc.cz(0, 2)

# Simulate
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()
counts = result.get_counts()

print("Teleportation Results:")
print(counts)

plot_histogram(counts)
plt.show()