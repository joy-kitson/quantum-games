#!/usr/bin/env python3
import numpy as np
import cmath
from math import pi

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer, execute, Aer, IBMQ
from qiskit.compiler import transpile
from qiskit.quantum_info.operators import Operator, Pauli
from qiskit.quantum_info import process_fidelity
from qiskit.extensions import RXGate, CnotGate, XGate

def create_entangle_matrix(gamma):
    half = gamma/2
    return np.matrix([
        [cmath.cos(half),    0,                  0,                   1j*cmath.sin(half)],
        [0,                  cmath.cos(half),   -1j*cmath.sin(half),  0                 ],
        [0,                 -1j*cmath.sin(half), cmath.cos(half),     0                 ],
        [1j*cmath.sin(half), 0,                  0,                   cmath.cos(half)   ]
    ])

def create_strategy_matrix(theta, phi):
    half = theta/2
    return np.matrix([
        [cmath.exp(1j*phi)*cmath.cos(half), cmath.sin(half)                   ],
        [-cmath.sin(half),                  cmath.exp(-1j*phi)*cmath.cos(half)]
    ])

def build_game_circuit(alice_strat, bob_strat, gamma):
    circuit = QuantumCircuit(2, 2)

    entangle = Operator(create_entangle_matrix(gamma))
    untangle = Operator(create_entangle_matrix(gamma).getH())

    circuit.append(entangle, [0, 1])
    circuit.append(Operator(alice_strat), [0])
    circuit.append(Operator(bob_strat), [1])
    circuit.append(untangle, [0, 1])
    circuit.measure([0, 1], [0, 1])

    return circuit

def run_circuit(circuit, backend=BasicAer.get_backend('qasm_simulator'), shots=1000):
    result = execute(circuit, backend, shots=shots).result()
    return result.get_counts()

# Standard payoff matrices
ALICE_PAY = {
    '00': 3,
    '01': 5,
    '10': 0,
    '11': 1
}
BOB_PAY = {
    '00': 3,
    '01': 0,
    '10': 5,
    '11': 1
}
# returns the expected payoff given a dict of counts and a dict of payoffs for each result
def get_payoff(counts, payoffs):
    expected_payoff = 0
    total = 0
    for outcome in counts:
        expected_payoff += counts[outcome] * payoffs[outcome]
        total += counts[outcome]

    return expected_payoff / total
