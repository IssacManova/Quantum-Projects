from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Hidden string
secret_string = "1011"
n = len(secret_string)

# Create circuit (n input + 1 output qubit)
qc = QuantumCircuit(n+1, n)

# Step 1: Initialize output qubit to |1>
qc.x(n)
qc.h(range(n+1))

# Step 2: Oracle encoding secret string
for i, bit in enumerate(secret_string):
    if bit == "1":
        qc.cx(i, n)

# Step 3: Apply Hadamard to input qubits
qc.h(range(n))

# Step 4: Measure input qubits
qc.measure(range(n), range(n))

# Run simulation
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()
counts = result.get_counts()

print("Bernstein-Vazirani Result:")
print(counts)

plot_histogram(counts)
plt.show()
