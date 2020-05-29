class Player:
    """
    Represents a player in a Tic, Tac, Toe game.
    """
    def __init__(self):
        self.side = None

    def choose_side(self):
        """
        Lets the player decide if they want to be 'X' or 'O'.

        Then modifies the `side` attribute.
        """
        while True:
            decision = input('Would you like to be \'X\' or \'O\'?\n').upper()

            # Validation of decision
            if decision not in 'XO' or len(decision) > 1 or not decision:
                print('\nPlease enter a correct response.')
                continue

            self.side = decision
            break

    @staticmethod
    def whose_turn(turn_num):
        """
        Returns whether it is Player 1 or Player 2's turn currently.

        NOTE: Player 1 always goes first.
        """
        if turn_num % 2:
            return 1
        return 2