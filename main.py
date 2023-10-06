import sys
from constants import GAME_MODES, START_MESSAGE, PLAY_WITH_COMPUTER, PLAY_WITH_HUMAN, EXIT_GAME
from game import Game

"""
Ends the session
"""
def end_game():
    print('Thanks for playing! Ka Kite.')
    sys.exit(0)

"""
Evaluate game and print current scores.
"""
def score_game(result, scores, play_with_human):
  if(result == 0):
    print('Draw!\n')
    scores['d'] += 1
  elif(result == 1):
    print('You won!\n')
    scores['p1'] += 1
  else:
    if play_with_human:
      print('You lost! Player 2 Wins!\n')
      scores['p2'] += 1
    else:
      print('You lost! Computer Wins!\n')
      scores['c'] += 1

  print('Current Scores')
  print('-----------------------------')
  print(f"Player 1: {scores['p1']}")
  print(f"{'Player 2' if play_with_human else 'Computer'}: {scores['p2'] if play_with_human else scores['c']}")
  print(f"Draws: {scores['d']}\n")

"""
Start Tic Tac Toe Game
"""
def start_game():
  print('\nKia Ora! and welcome to Andre\'s Tic Tac Toe Game')
  print('----------------------------------------------------')
  scores = { 'p1': 0, 'p2': 0, 'c': 0, 'd': 0 }
  option = input(START_MESSAGE)
  while option not in GAME_MODES:
    print('Oops that option is not available\n')
    option = input(START_MESSAGE)

  if(option == PLAY_WITH_HUMAN):
    play_with_human = True
  elif(option == PLAY_WITH_COMPUTER):
    play_with_human = False
  elif(option == EXIT_GAME):
    end_game()

  num_games = 1
  game = Game(play_with_human=play_with_human)
  print(f'Game {num_games}')
  num_games+= 1
  result = game.start()
  score_game(result=result, scores=scores, play_with_human=play_with_human)

  option = input('Press Enter to play again, or type \'exit\' to quit\n')
  if(option == EXIT_GAME): sys.exit(0)
  while option != EXIT_GAME or option == '':
    print(f'Game {num_games}')
    result = game.start()
    score_game(result=result, scores=scores, play_with_human=play_with_human)
    num_games+= 1
    option = input('Press Enter to play again, or type \'exit\' to quit\n')
    if(option == EXIT_GAME): sys.exit(0)

if __name__ == '__main__':
  start_game()