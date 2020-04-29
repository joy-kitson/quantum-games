#!/usr/bin/env python3
from pd_base import *

# An interface defining what a bot for our PD games needs to be able to do
class Bot:
    def get_strategy():
        pass

    def process_results(counts, payoff, player_num):
        pass

class TitForTatBot(Bot):
    def get_strategy():
        pass

    def process_results(counts, payoff, player_num):
        pass

class MiracleMoveBot(Bot):
    def get_strategy():
        pass

    def process_results(counts, payoff, player_num):
        pass
