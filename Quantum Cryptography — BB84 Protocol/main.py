import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def bb84_protocol(n_bits=20):
    alice_bits = [random.randint(0, 1) for _ in range(n_bits)]
    alice_bases = [random.choice(['Z', 'X']) for _ in range(n_bits)]
    bob_bases = [random.choice(['Z', 'X']) for _ in range(n_bits)]

    simulator = AerSimulator()
    bob_results = []

    for i in range(n_bits):
        qc = QuantumCircuit(1, 1)

        if alice_bits[i] == 1:
            qc.x(0)
        if alice_bases[i] == 'X':
            qc.h(0)

        if bob_bases[i] == 'X':
            qc.h(0)

        qc.measure(0, 0)

        compiled = transpile(qc, simulator)
        result = simulator.run(compiled, shots=1).result()
        bob_results.append(int(list(result.get_counts().keys())[0]))

    key = []
    for i in range(n_bits):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_bits[i])

    return key

if __name__ == "__main__":
    secret_key = bb84_protocol()
    print("Generated Secret Key:")
    print(secret_key)