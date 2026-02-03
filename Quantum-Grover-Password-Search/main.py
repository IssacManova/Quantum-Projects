from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Number of qubits (2 qubits → 4 possible passwords)
n_qubits = 2

# Target state (password)
target_state = "11"

def grover_oracle():
    qc = QuantumCircuit(n_qubits)
    
    # Flip phase of |11>
    qc.cz(0, 1)
    
    return qc

def diffusion_operator():
    qc = QuantumCircuit(n_qubits)
    
    qc.h(range(n_qubits))
    qc.x(range(n_qubits))
    qc.h(n_qubits - 1)
    qc.cx(0, 1)
    qc.h(n_qubits - 1)
    qc.x(range(n_qubits))
    qc.h(range(n_qubits))
    
    return qc

# Main circuit
qc = QuantumCircuit(n_qubits, n_qubits)

# Step 1: Superposition
qc.h(range(n_qubits))

# Step 2: Oracle
qc.compose(grover_oracle(), inplace=True)

# Step 3: Diffusion
qc.compose(diffusion_operator(), inplace=True)

# Step 4: Measurement
qc.measure(range(n_qubits), range(n_qubits))

# Run simulation
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()
counts = result.get_counts()

print("Grover Search Output:")
print(counts)

plot_histogram(counts)
plt.show()