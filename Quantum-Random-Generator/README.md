# Quantum Random Number Generator ⚛️

## Overview
This project demonstrates a Quantum Random Number Generator (QRNG) using Qiskit.
Unlike classical pseudo-random generators, this project uses quantum superposition
and measurement to generate true randomness.

## Concepts Used
- Qubits and Superposition
- Hadamard Gate
- Quantum Measurement
- Quantum Simulation using Qiskit Aer

## How It Works
1. A qubit is initialized in the |0⟩ state.
2. A Hadamard gate places the qubit in superposition.
3. The qubit is measured multiple times.
4. Measurement results are collected and visualized.

## Technologies
- Python 3.11
- Qiskit
- Qiskit Aer
- Matplotlib

## Output
The output shows an approximately 50-50 distribution of 0s and 1s,
demonstrating quantum randomness.

## Future Improvements
- Generate multi-bit quantum random numbers
- Save outputs to CSV
- Compare with classical random generators