#!/usr/bin/env python3
import cmath

from pd_base import *

# An interface defining what a bot for our PD games needs to be able to do
class Bot:
    def get_strategy(self):
        pass

    def process_results(self, counts, payoff, player_num):
        pass

class TitForTatBot(Bot):
    COOPERATE = create_strategy_matrix(0, 0)
    DEFECT = create_strategy_matrix(cmath.pi, cmath.pi)

    def __init__(self):
        self.next_move = TitForTatBot.COOPERATE

    def get_strategy(self):
        return self.next_move

    def process_results(self, counts, payoff, player_num):
        #TODO: verify representation of moves

        defect_count, coop_count = 0, 0
        for outcome in counts:
            if outcome[player_num] == '0':
                coop_count += counts[outcome]
            else:
                defect_count += counts[outcome]

        # If one count is higher than the other, change our response to match it
        if defect_count > coop_count:
            self.next_move = TitForTatBot.DEFECT
        elif defect_count < coop_count:
            self.next_move = TitForTatBot.COOPERATE

class MiracleMoveBot(Bot):
    MIRACLE_MOVE = create_strategy_matrix(cmath.pi/2,cmath.pi/2)
    
    def get_strategy(self):
        return MiracleMoveBot.MIRACLE_MOVE

    def process_results(self, counts, payoff, player_num):
        pass
