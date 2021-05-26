import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter
        pass

    # we want alll player to get their next move given a game
    def get_move(seft, game):
        pass

    pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(seft, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

    pass
     
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(seft, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(seft.letter + '\'s turn. Input move (0-8):')
            # we're going to check that this is a correct value by trying to cast
            # it to an interger, and if it's not, then wa say its invalid
            # if that spot is not acailable on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')

        return val

    pass