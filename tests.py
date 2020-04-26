import unittest
from clr import Player, Game

class TestGameMethods(unittest.TestCase):
  def setUp(self):
    self.game = Game()
  
  def test_add_player(self):
    self.game.add_player('Matt')
    num_players = len(self.game.players)
    self.assertEqual(num_players, 1, f'Added 1 player but there are {num_players} showing.')
    self.assertEqual(self.game.players[0].name, 'Matt', f'Expected player 0 name to be Matt but got {self.game.players[0].name}')

  def test_reset_game(self):
    self.game.add_player('Matt')
    self.game.add_player('Matt2')
    self.game.add_player('Matt3')
    self.game.add_player('Matt4')
    
    self.game.players[0].tokens = 1
    self.game.players[1].tokens = 2
    self.game.players[2].tokens = 3
    self.game.players[3].tokens = 4
    
    self.game.center = 5

    self.game.reset_game()
    self.assertEqual([], self.game.players, f'Expected reset to result in no players, but there are players')
    self.assertEqual(self.game.num_players, 0)
    self.assertEqual(self.game.center, 0, f'Expecting center pot to be 0 but got {self.game.center}')

  def test_move_tokens(self):
    self.game.reset_game()

    self.game.add_player('Test 0')
    self.game.add_player('Test 1')

    self.assertEqual(self.game.players[0].tokens, 3, f'Expected player 0 to have 3 tokens but has {self.game.players[0].tokens}')
    self.assertEqual(self.game.players[1].tokens, 3, f'Expected player 1 to have 3 tokens but has {self.game.players[1].tokens}')
    
    self.game.move_tokens(0, 1)
    self.assertEqual(self.game.players[0].tokens, 2, f'After moving tokens from Player 0 to Player 1, expected Player 0 to have 2 tokens but has {self.game.players[0].tokens}')
    self.assertEqual(self.game.players[1].tokens, 4, f'After moving tokens from Player 0 to Player 1, expected Player 1 to have 4 tokens but has {self.game.players[1].tokens}')
    
    self.game.move_tokens(0, 1)
    self.game.move_tokens(0, 1)
    self.assertEqual(self.game.players[0].tokens, 0, f'After moving 3 tokens from Player 0 to Player 1, expected Player 0 to have 0 tokens but has {self.game.players[0].tokens}')
    self.assertEqual(self.game.players[1].tokens, 6, f'After moving tokens from Player 0 to Player 1, expected Player 1 to have 6 tokens but has {self.game.players[1].tokens}')
    
    self.game.move_tokens(0, 1)
    self.assertEqual(self.game.players[0].tokens, 0, f'After attempting to move tokens when empty from player 0 to player 1, expected Player 0 to have 0 tokens but has {self.game.players[0].tokens}')
    self.assertEqual(self.game.players[1].tokens, 6, f'After attempting to move tokens when empty from player 0 to player 1, expected Player 1 to have 6 tokens but has {self.game.players[1].tokens}')
    

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

  def test_roll_all_dice(self):
    values_allowed = ['•', 'L', 'C', 'R']

    self.player0.roll_all_dice()
    self.player0.dice
    self.assertEqual(self.player0.dice, [None, None, None], f'Expected no rolls for player with no tokens.')

    self.player1.roll_all_dice()
    self.player1.dice
    self.assertIn(self.player1.dice[0], values_allowed, f'Dice roll produced {self.player1.dice[0]} which is not an expected value.')
    self.assertEqual(self.player1.dice[1], None, f'Expected 1 token player to only have 1 dice value.')
    self.assertEqual(self.player1.dice[2], None, f'Expected 1 token player to only have 1 dice value.')

    self.player2.roll_all_dice()
    self.player2.dice
    self.assertIn(self.player2.dice[0], values_allowed, f'Dice roll produced {self.player2.dice[0]} which is not an expected value.')
    self.assertIn(self.player2.dice[1], values_allowed, f'Dice roll produced {self.player2.dice[1]} which is not an expected value.')
    self.assertEqual(self.player2.dice[2], None, f'Expected 2 token player to only have 2 dice values.')

    self.player3.roll_all_dice()
    self.player3.dice
    self.assertIn(self.player3.dice[0], values_allowed, f'Dice roll produced {self.player3.dice[0]} which is not an expected value.')
    self.assertIn(self.player3.dice[1], values_allowed, f'Dice roll produced {self.player3.dice[1]} which is not an expected value.')
    self.assertIn(self.player3.dice[2], values_allowed, f'Dice roll produced {self.player3.dice[2]} which is not an expected value.')
    
if __name__ == '__main__':
  unittest.main()


