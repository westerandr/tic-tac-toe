"""
Constants to use for Game String literals with some Exceptions for handling bad player moves.
"""
START_MESSAGE = 'Enter \'1\' to play with a person (2 Players)\nEnter \'2\' to play the Computer\nType \'exit\' to quit the game\n'
PLAY_WITH_HUMAN = '1'
PLAY_WITH_COMPUTER = '2'
EXIT_GAME = 'exit'
GAME_MODES = ['1', '2', 'exit']
MOVES = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

class InvalidMoveException(Exception):
  pass

class SquareOccupiedException(Exception):
  pass