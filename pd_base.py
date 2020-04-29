#!/usr/bin/env python3
import numpy as np
import cmath
from math import pi

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

def get_payoff(counts, payoffs):
    # returns the expected payoff given a dict of counts for each result: [00, 01, 10, 11]
    # and a dict of payoffs for each result

    expected_payoff = 0
    total = 0
    for outcome in counts:
        expected_payoff += counts[outcome] * payoffs[outcome]
        total += counts[outcome]

    return expected_payoff / total
