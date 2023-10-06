from constants import MOVES, InvalidMoveException, SquareOccupiedException, EXIT_GAME
import random, sys

class Game():

  """
  Constructor Setup
  """
  def __init__(self, play_with_human) -> None:
    self.current_turn = 1
    self.play_with_human = play_with_human
    self.board = { 'A1': '-', 'A2': '-', 'A3': '-',  'B1': '-', 'B2': '-', 'B3': '-',  'C1': '-', 'C2': '-', 'C3': '-'}
    self.this_player = 'Player 1' if play_with_human else 'Player'
    self.other_player = 'Player 2' if play_with_human else 'Computer'
    self.stopped = False
    self.result = -1

    """
    Allows the player to select a move and then checks for a winning move or draw.
    """
  def select_square(self):
    available_squares = self.get_available_squares()

    # Check if computer
    if not self.play_with_human and self.current_turn == 2:
      move = random.choice(available_squares)

      while not self.check_valid_move(move, available_squares):
        move = random.choice(available_squares)
      print(f"Computer selected {move}")

    else:
      move = input(f'Enter move (Available Moves: {", ".join(available_squares)}) \n')
      if(move == EXIT_GAME): sys.exit(0)

      while not self.check_valid_move(move, available_squares):
        self.print_current_turn()
        move = input(f'Enter move ({", ".join(available_squares)}) \n')
        if(move == EXIT_GAME): sys.exit(0)

    self.board[move] = self.get_player_piece()

    winner = self.check_winning_move()
    if(winner):
      self.winner()

    if(self.check_for_draw(winner)):
      self.stopped = True
      self.result = 0

    self.end_turn()

    """
    Get Available Squares on the Board
    """
  def get_available_squares(self):
    board = self.board
    valid_moves = []
    for item in board.items():
      if(item[1] == '-'):
        valid_moves.append(item[0])
    return valid_moves

  """
  Check if the move chosen is valid i.e. not out of board bounds, is not occupied already.
  """
  def check_valid_move(self, move, available_squares):
    try:
      if move not in MOVES:
        raise InvalidMoveException
      if not self.is_valid_move(move):
        raise SquareOccupiedException
    except InvalidMoveException:
      print(f'Move is not valid, please select a value from {", ".join(available_squares)}')
    except SquareOccupiedException:
      print(f"That square is occupied. Please try again")
    else:
      return move in MOVES and self.is_valid_move(move)

  """
  Checks if the square is not occupied
  """
  def is_valid_move(self, option):
    return self.board[option] == '-'

  """
  Change Current Player Index
  """
  def end_turn(self):
    if(self.current_turn == 1):
      self.current_turn = 2
    else:
      self.current_turn = 1

  """
  Get current player's piece to set on board.
  """
  def get_player_piece(self):
    if(self.current_turn == 1):
      return 'X'
    else:
      return 'O'

  """
  Set winner conditions
  """
  def winner(self):
    self.stopped = True
    self.result = self.current_turn

  """
  Check for a draw on the board. No winner and all spots occupied.
  """
  def check_for_draw(self, winner):
    if(not winner):
      current_moves = list(self.board.values())
      for cm in current_moves:
        if cm == '-':
          return False
      return True
    return False

  """
  Check for a winner
  """
  def check_winning_move(self):
    board = self.board
    if((board[MOVES[0]] != '-' and board[MOVES[0]] == board[MOVES[1]] == board[MOVES[2]]) or
    (board[MOVES[3]] != '-' and  board[MOVES[3]] == board[MOVES[4]] == board[MOVES[5]]) or
    (board[MOVES[6]] != '-' and board[MOVES[6]] == board[MOVES[7]] == board[MOVES[8]]) or
    (board[MOVES[0]] != '-' and board[MOVES[0]] == board[MOVES[3]] == board[MOVES[6]]) or
    (board[MOVES[1]] != '-' and board[MOVES[1]] == board[MOVES[4]] == board[MOVES[7]]) or
    (board[MOVES[2]] != '-' and board[MOVES[2]] == board[MOVES[5]] == board[MOVES[8]]) or
    (board[MOVES[0]] != '-' and board[MOVES[0]] == board[MOVES[4]] == board[MOVES[8]]) or
    (board[MOVES[4]] != '-' and board[MOVES[2]] == board[MOVES[4]] == board[MOVES[6]])):
      return True
    return False

  """
  Print Current Player's Turn.
  """
  def print_current_turn(self):
    if(self.current_turn == 1):
      print(f"{self.this_player}'s Turn")
    else:
      print(f"{self.other_player}'s Turn")
    print('--------------------------------')

  """
  Reset Game State
  """
  def reset(self):
    self.current_turn = 1
    self.board = { 'A1': '-', 'A2': '-', 'A3': '-',  'B1': '-', 'B2': '-', 'B3': '-',  'C1': '-', 'C2': '-', 'C3': '-'}
    self.stopped = False
    self.result = -1

  """
  Display Board to Terminal
  """
  def print_board(self):
    board = self.board
    print(f"| {board['A1']} | {board['A2']} | {board['A3']} |")
    print(f"| {board['B1']} | {board['B2']} | {board['B3']} |")
    print(f"| {board['C1']} | {board['C2']} | {board['C3']} |")

  """
  Welcome Message to User
  """
  def welcome(self):
    print('To start select a square on the board')
    print(f"| A1 | A2 | A3 |")
    print(f"| B1 | B2 | B3 |")
    print(f"| C1 | C2 | C3 |\n")

  """
  Start Tic Tac Toe Game
  """
  def start(self):
    self.reset()
    self.welcome()
    while not self.stopped:
      self.print_current_turn()
      self.select_square()
      self.print_board()
    return self.result