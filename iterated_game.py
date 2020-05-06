#!/usr/bin/env python3
# coding: utf-8

from pd_base import *
from bots import *

# Loading your IBM Q account(s)
provider = IBMQ.load_account()

alice = MiracleMoveBot()
bob = TitForTatBot()

def run_iterated_game(\
        players,\
        payoff_matrices=[ALICE_PAY, BOB_PAY],\
        num_rounds=10,\
        gamma=.5):
    
    total_payoffs = [0 for p in players]
    
    for round in range(num_rounds):
        circuit = build_game_circuit(\
                players[0].get_strategy(),\
                players[1].get_strategy(),\
                gamma)
        counts = run_circuit(circuit, shots=1000)
        
        for i in range(len(players)):
            payoff = get_payoff(counts, payoff_matrices[i])
            players[i].process_results(counts, payoff, i)
            
            total_payoffs[i] += payoff
    
    return total_payoffs

print(run_iterated_game([alice, bob]))
