import random

class Player():

  def __init__(self, name, player_position = None):
    self.name = name
    self.num_rolls = 3
    self.tokens = 3
    self.player_position = player_position
    self.dice = [0,0,0]

  def __repr__(self):
    return f'Player {self.name} in position {self.player_position} with {self.tokens} tokens'

  def calculate_rolls(self):
    if self.tokens >= 3:
      self.num_rolls = 3
    else:
      self.num_rolls = self.tokens

  def roll_dice(self):
    """
    Rolls the dice in a CLR game
    """
    dice_values = {1: '•', 2: '•', 3: '•', 4: 'L', 5: 'C', 6: 'R'}
    result = random.randint(1, 6)

    return dice_values[result]

  def roll_all_dice(self):
    """
    Rolls all dice
    """

    self.calculate_rolls()
    if self.num_rolls > 0:
      for i in range(0,self.num_rolls):
        self.dice[i] = self.roll_dice()
      if self.num_rolls == 1:
        self.dice[1] = None
        self.dice[2] = None
      if self.num_rolls == 2:
        self.dice[2] = None
    else:
      self.dice = [None, None, None]

class Game():

  def __init__(self):
    self.num_players = 0
    self.players = []
    self.center = 0

    print('Welcome to CLR!')
    self.initialize_game()

  def initialize_game(self):
    try:
      self.num_players = int(input('How many players are playing? '))
    except:
      print('Please enter a valid number of players.')
      self.initialize_game()

    for i in range(0,self.num_players):
      player_name = input(f'What is the name of player {i + 1}? ')
      new_player = Player(name = player_name, player_position = i)
      self.players.append(new_player)

    print(self.players)

if __name__ == '__main__':
    new_game = Game()