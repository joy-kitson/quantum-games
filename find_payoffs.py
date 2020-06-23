#!/usr/bin/env python3
# coding: utf-8

import argparse
from iterated_game import run_iterated_game
import os

def main():
    alice_filename = 'alice_payoffs.csv'
    bob_filename = 'bob_payoffs.csv'
    m_pows = range(4)
    n_pows = range(5)
 
    with open(alice_filename, 'w') as alice_file:
        with open(bob_filename, 'w') as bob_file:
            # Add header for columns
            alice_file.write(',' + ','.join([str(2 ** n_pow) for n_pow in n_pows]) + '\n')
            bob_file.write(',' + ','.join([str(2 ** n_pow) for n_pow in n_pows]) + '\n')
            
            num_games = 10
            for m_pow in m_pows:
                m = 2 ** m_pow
                
                # Add header for each row
                alice_file.write('{},'.format(m))
                bob_file.write('{},'.format(m))

                for n_pow in n_pows:
                    n = 2 ** n_pow
                    payoffs = run_iterated_game(num_games=num_games, num_rounds=n, shots=m)
                    print('n = {}, m = {}, ({},{})'.format(n, m, payoffs[0], payoffs[1]))
                    alice_file.write('{},'.format(payoffs[0]))
                    bob_file.write('{},'.format(payoffs[1]))

                # End the row
                alice_file.write('\n')
                bob_file.write('\n')

if __name__ == '__main__':
    main()
