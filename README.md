# Flappy-Bird-NEAT-Python

# About The Project

This is a clone of flappy bird game incorporated with [NEAT](https://neat-python.readthedocs.io/en/latest/)(NeuroEvolution of Augmenting Topologies)-Python. The position of the bird, top pipe and bottom pipe is fed to NEAT-Python to create artificial neural networks and determine when to jump. 

# Built With

- NEAT-Python
- Pygame

# Getting Started

Download this project and simply run [FlappyBird.py](http://flappybird.py) file. config-feedforward.txt file can be modified to give different results.

### Some Parameters to play around:

- `pop-size` The number of birds in each generation.
- `bias_mutate_rate` The probability that mutation will change the bias of a node by adding a random value
- `bias_replace_rate` The probability that mutation will replace the bias of a node with a newly chosen random value