from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

print("Program started...")

def generate_random_bits(shots=1024):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    simulator = AerSimulator()
    compiled = transpile(qc, simulator)
    result = simulator.run(compiled, shots=shots).result()
    counts = result.get_counts()

    return counts

if __name__ == "__main__":
    shots = 1000
    counts = generate_random_bits(shots)

    print("Quantum Random Output:")
    print(counts)

    plot_histogram(counts)
    plt.show()
