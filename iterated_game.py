#!/usr/bin/env python3
# coding: utf-8

from pd_base import *
from bots import *
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    # Required arguments:
    parser.add_argument(
        'num_games', metavar='g', type=int, help='The number of games to average payoffs over'
    )
    parser.add_argument(
        'num_rounds', metavar='n', type=int, help='The number of rounds to play in each game'
    )
    parser.add_argument(
        'shots', metavar='m', type=int, help='The number of measurements to make in each round'
    )

    return parser.parse_args()

def run_iterated_game(
        init_players=[MiracleMoveBot, TitForTatBot],
        payoff_matrices=[ALICE_PAY, BOB_PAY],
        num_games=1,
        num_rounds=10,
        gamma=.5,
        shots=1,
        normalised=True):
    
    total_payoffs = [0 for p in init_players]
    
    for game in range(num_games):
        players = [init() for init in init_players]
        
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
   
    # Average the results of the games
    if normalised:
        total_payoffs = [p / (num_games * num_rounds) for p in total_payoffs]

    else:
        total_payoffs = [p / num_games for p in total_payoffs]

    return total_payoffs

def main():
    args = parse_args()

    # Loading your IBM Q account(s)
    provider = IBMQ.load_account()

    print('Alice is a MiracleMoveBot')
    print('Bob is a TitForTatBot')

    payoffs = run_iterated_game(
        num_games=args.num_games,
        num_rounds=args.num_rounds,
        shots=args.shots,
    )

    print("Alice's Payoff:", payoffs[0])
    print("Bob's Payoff:", payoffs[1])

if __name__ == '__main__':
    main()
