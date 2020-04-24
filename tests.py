import unittest
from clr import Player

class TestPlayerMethods(unittest.TestCase):
  def setUp(self):
    self.player0 = Player(name = 'Test Player 0')
    self.player1 = Player(name = 'Test Player 1')
    self.player2 = Player(name = 'Test Player 2')
    self.player3 = Player(name = 'Test Player 3')
    self.player4 = Player(name = 'Test Player 4')
    self.player5 = Player(name = 'Test Player 5')

    self.player0.tokens = 0
    self.player1.tokens = 1
    self.player2.tokens = 2
    self.player3.tokens = 3
    self.player4.tokens = 4
    self.player5.tokens = 5
    
  def test_calculate_rolls(self):
    p = self.player1
    p.tokens = 0
    p.calculate_rolls()

    self.assertEqual(p.num_rolls, 0, f'Player has {p.num_rolls} rolls but should have 0')

    p.tokens = 1
    p.calculate_rolls()
    self.assertEqual(p.num_rolls, 1, f'Player has {p.num_rolls} rolls but should have 1')

    p.tokens = 2
    p.calculate_rolls()
    self.assertEqual(p.num_rolls, 2, f'Player has {p.num_rolls} rolls but should have 2')

    p.tokens = 3
    p.calculate_rolls()
    self.assertEqual(p.num_rolls, 3, f'Player has {p.num_rolls} rolls but should have 3')

    p.tokens = 4
    p.calculate_rolls()
    self.assertEqual(p.num_rolls, 3, f'Player has {p.num_rolls} rolls but should have 3')

    p.tokens = 20
    p.calculate_rolls()
    self.assertEqual(p.num_rolls, 3, f'Player has {p.num_rolls} rolls but should have 3')

  def test_roll_dice(self):
    one_rolls = self.player1.roll_dice()
    values_allowed = ['•', 'L', 'C', 'R']
    self.assertIn(one_rolls, values_allowed, f'Dice roll produced {one_rolls} which is not an expected value.')


if __name__ == '__main__':
  unittest.main()


