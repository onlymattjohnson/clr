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

  def add_player(self, player_name = None):
    num_players = len(self.players)
    if not player_name:
      player_name = input(f'What is the name of player {num_players + 1}? ')
    new_player = Player(name = player_name, player_position = num_players)
    self.players.append(new_player)

  def start_game(self):
    try:
      self.num_players = int(input('How many players are playing? '))
    except:
      print('Please enter a valid number of players.')
      self.initialize_game()

    for i in range(0,self.num_players):
      self.add_player()

    print(self.players)

  def move_tokens(self, player_from, player_to):
    if self.players[player_from].tokens > 0:
      self.players[player_from].tokens = self.players[player_from].tokens - 1
      if player_to == 'C':
        self.center = self.center + 1
      else:
        self.players[player_to].tokens = self.players[player_to].tokens + 1
    
  def move_tokens_by_direction(self, player_from, direction):
    if direction == 'L':
      player_to = player_from - 1
    if direction == 'R':
      player_to = player_from + 1
      if player_to == len(self.players):
        player_to = 0
    if direction == 'C':
      player_to = 'C'
    
    self.move_tokens(player_from = player_from, player_to = player_to)

  def reset_game(self):
    self.num_players = 0
    self.players = []
    self.center = 0

if __name__ == '__main__':
    new_game = Game()
    new_game.start_game()