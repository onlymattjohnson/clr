import random

def roll_dice():
  """
  Rolls the dice in a CLR game
  """
  dice_values = {1: '•', 2: '•', 3: '•', 4: 'L', 5: 'C', 6: 'R'}
  result = random.randint(1, 6)

  return dice_values[result]

if __name__ == '__main__':
    dice1 = roll_dice()
    dice2 = roll_dice()
    dice3 = roll_dice()

    print(dice1, dice2, dice3)