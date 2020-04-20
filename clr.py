import random

class Player():

  def __init__(self, name):
    self.name = name
    self.tokens = 3

  def roll_dice(self):
    """
    Rolls the dice in a CLR game
    """
    dice_values = {1: '•', 2: '•', 3: '•', 4: 'L', 5: 'C', 6: 'R'}
    result = random.randint(1, 6)

    return dice_values[result]

if __name__ == '__main__':
    new_player = Player(name = 'Matt')
    dice1 = new_player.roll_dice()
    dice2 = new_player.roll_dice()
    dice3 = new_player.roll_dice()

    print(dice1, dice2, dice3)