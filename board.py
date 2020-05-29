class Board:
    """
    Represents a Tic, Tac, Toe board.
    """
    def __init__(self):
        self.coordinates = None

    def __str__(self):
        """
        Returns a string which represents the board, row by row.
        """
        rows = ''
        for i in range(0, 9, 3):
            for square in self.coordinates[i: i + 3]:
                # A space is put to separate each square since Python doesn't
                # have a constant for whitespace
                rows += f'{square} '
            rows += '\n'
        return rows

    def make_board(self):
        """
        Modifies the `coordinates` attribute and makes a 1D array, which
        is the initial state of the board.
        """
        self.coordinates = ['.' for i in range(9)]

    def validate_move(self, move):
        """
        Validates `move` by making sure that the square is empty
        and that the coordinate is not outside of the board.

        Also makes sure that the move is a non-negative integer.

        Returns True for a valid move.
        """
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                if self.coordinates[move - 1] == '.':
                    return True
        return False

    def get_move(self):
        """
        Gets the move from the user as input, validates it and then
        returns the move as an integer.
        """
        while True:
            move = input('''Please choose the square that you would like to place
your marker on (from 1 - 9): ''')

            if not self.validate_move(move):
                print('Please enter a valid coordinate.\n')
                continue
            # We subtract 1, as the index for the first square is 0 but we present
            # it as 1 for the user to make input easier and from 1 - 9
            return int(move) - 1

    def insert_move(self, move, player_current):
        """
        Places 'X' or 'O' (depends on `player_current`) on the given
        coordinates (from `move`); this is done by modifying the
        `coordinates` attribute.
        """
        self.coordinates[move] = player_current

    def game_state(self):
        """
        Returns 0 if the winner is 'X' or 1 if the winner is 'O', after
        looking through the board and seeing if there is a won
        position.

        If there is no won position, returns 2 if ongoing and 3 if draw.
        """
        won_combinations = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        )
        for comb in won_combinations:
            a, b, c = comb
            a_val, b_val, c_val = self.coordinates[a], self.coordinates[b], self.coordinates[c]
            if a_val == b_val == c_val and '.' not in (a_val, b_val, c_val):
                if self.coordinates[a] == 'X':
                    # 'X' victory
                    return 0
                # 'O' victory
                return 1

        for i in range(0, 9, 3):
            if '.' in self.coordinates[i: i + 3]:
                # There are still unfilled squares so the game is unfinished
                return 2
        # Only other possibility is a draw
        return 3