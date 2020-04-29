#!/usr/bin/env python3
from pd_base import *

# An interface defining what a bot for our PD games needs to be able to do
class bot:
    def get_strategy():
        pass

    def process_results(counts, payoff, player_num):
        pass
