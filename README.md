# The Quantum Prisioner's Dilemma
This repo contains code used for a paper on the Quantum Prisioner's Dilemma (QPD), a generalization of the seminal [classical game](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma).

## File Types:

### Libraries
These files aren't designed to be run independently, but rather to imported as a library by other programs in the repo.

#### `pd_base.py`
This library contains many of the function used in other files to create quantum gates and ciruits, run ciruits, and calculate a player's payoff based on the results of a run. 

#### `bots.py`
This library contains several classes used to define the behavior of players (or "bots") in an iterated version of the QPD.

### Scripts
These files are designed to be run from the command line. They can be run with `python3 <filename>`, or, if you're working on a unix system, `./<filename>`. In either case, this command should be followed by any any necessary arguments, seperated by spaces.

#### `iterated_game.py`
This run an iterated QPD game between two players, using the strategies definied in `bots.py`. The first player, Alice, uses the miracle move (see the paper for details) and the second, Bob, uses a version of [tit-for-tat](https://en.wikipedia.org/wiki/Tit_for_tat) adapted for the QPD.

This script requires two command line arguments:
1. The number of rounds the iterated game should last.
2. The number of times each quantum circuit is run to calculate the results of a measurement
and can be run as. This is refered to as the number of shots.
  ```python3 iterated_game.py <num rounds> <num shots>```
or
  ```./iterated_game.py <num rounds> <num shots>```

### iPython Notebooks
iPython Notebooks combine code with its output, including in-line graphics produced by the program. You can look at this code using tools like iPython or (Jupyter)[https://jupyter.org/], which allow code notebooks to be run and edited. If you are unfamiliar with how to use Jupyter notebooks there are [plenty](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) of [good tutorials](https://www.tutorialspoint.com/jupyter/index.htm) out there.

#### `apay.ipynb`
This notebook which is used to generate several plots depicting the expected payoff of strategies in the QPD.

#### `real_qc.ipynb`
This notebook is used to find which of the various IBM quantum computers are available.
