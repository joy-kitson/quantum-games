#!/usr/bin/env python3
# coding: utf-8

from pd_base import *
from bots import *
import sys

def run_iterated_game(\
        players,\
        payoff_matrices=[ALICE_PAY, BOB_PAY],\
        num_rounds=10,\
        gamma=.5,
        shots=1):
    
    total_payoffs = [0 for p in players]
    
    for round in range(num_rounds):
        circuit = build_game_circuit(\
                players[0].get_strategy(),\
                players[1].get_strategy(),\
                gamma)
        counts = run_circuit(circuit, shots=shots)
        
        for i in range(len(players)):
            payoff = get_payoff(counts, payoff_matrices[i])
            players[i].process_results(counts, payoff, i)
            
            total_payoffs[i] += payoff
    
    return total_payoffs

def main():
    num_rounds = int(sys.argv[1])
    shots = int(sys.argv[2])
    
    # Loading your IBM Q account(s)
    provider = IBMQ.load_account()

    print('Alice is a MiracleMoveBot')
    alice = MiracleMoveBot()

    print('Bob is a TitForTatBot')
    bob = TitForTatBot()

    payoffs = run_iterated_game([alice, bob], num_rounds=num_rounds, shots=shots)

    print("Alice's Payoff:", payoffs[0])
    print("Bob's Payoff:", payoffs[1])

if __name__ == '__main__':
    main()
