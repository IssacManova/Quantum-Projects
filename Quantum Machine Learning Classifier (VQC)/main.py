import numpy as np
from qiskit.circuit.library import ZZFeatureMap
from qiskit.circuit.library import TwoLocal
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.utils import algorithm_globals
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from qiskit_aer import AerSimulator

# Set randomness seed
algorithm_globals.random_seed = 42

# Generate dataset
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_classes=2,
    n_redundant=0
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Feature map
feature_map = ZZFeatureMap(feature_dimension=2, reps=2)

# Variational circuit
ansatz = TwoLocal(2, ['ry', 'rz'], 'cz', reps=2)


from qiskit_machine_learning.optimizers import COBYLA

vqc = VQC(
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=COBYLA(maxiter=50)
)


# Train model
vqc.fit(X_train, y_train)

# Test accuracy
score = vqc.score(X_test, y_test)
print("Quantum Classifier Accuracy:", score)