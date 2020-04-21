def make_board():
    """
    Returns a tic tac toe board (1D array).
    """
    board = ['.' for i in range(9)]

    return board


def print_board(board):
    """
    Prints out the board row by row, 3 elements
    at a time.
    """
    for i in range(0, 9, 3):
        print(*board[i: i + 3])


def validate_move(move, board):
    """
    Validates the move by making sure that the square is empty
    and that the coordinate is not outside of the board.

    Also makes sure that the movie is a non-negative integer.

    Returns True for a valid move.
    """
    if move.isdigit():
        move = int(move)
        if 1 <= move <= 9:
            if board[move - 1] == '.':
                return True
    return False


def get_move(board):
    """
    Gets the move from the user as input and validates it and then
    returns the move as an integer
    """
    while True:
        move = input('''Please choose the square that you would like to place
your marker on (from 1 - 9): ''')

        if not validate_move(move, board):
            print('Please enter a valid coordinate.\n')
            continue

        # We subtract 1 as the index for the first square is 0
        # but we present it as 1 for the user to make input
        # easier and from 1 - 9
        return int(move) - 1


def insert_move(move, board, player_current):
    """
    Places 'X' or 'O' (depends on `player_current`) on the given
    coordinate (move), and then returns the new version of the
    board.
    """
    board[move] = player_current
    return board


def game_state(board):
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
        a_val, b_val, c_val = board[a], board[b], board[c]
        if a_val == b_val == c_val and '.' not in (a_val, b_val, c_val):
            if board[a] == 'X':
                # 'X' victory
                return 0
            # 'O' victory
            return 1

    for i in range(0, 9, 3):
        if '.' in board[i: i + 3]:
            # There are still unfilled squares so the game
            # is unfinished.
            return 2

    # Only other possibility is a draw
    return 3


def choose():
    """
    Lets the player decide if they want to be 'X' or 'O'.

    Then returns that decision
    """
    while True:
        decision = input('Would you like to be \'X\' or \'O\'?\n').upper()

        # Validation of decision
        if decision not in 'XO' or len(decision) > 1 or not decision:
            print('\nPlease enter a correct response.')
            continue

        return decision


def whose_turn(turn_num):
    """
    Returns whether it is Player 1 or Player 2's turn.

    NOTE: Player 1 always goes first.
    """
    if turn_num % 2:
        return 1
    return 2


def print_intro():
    """
    Prints the introduction, rules and controls of the game.
    """
    print('''\nWelcome to Tic, Tac, Toe! Let's get started with some rules!\n
The aim of the game is to make your marker (X or O) make a diagonal, vertical
or horizontal line with the rest of your markers. If you do so then you win.
Otherwise the game is a draw.
        
The way that the game is structured is that you will take turns placing
your markers and will be asked to input a number between 1 to 9. Where
that number represents the square on the board, like so:
        
1 2 3
4 5 6
7 8 9
        
Now let's get started!''')


def main():
    # print_intro()

    # Sets up the board and the players
    board = make_board()
    turn_num = 1
    player_1 = choose()
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    # To visually separate the start of the game from the rules
    print()

    # While the game is ongoing (2)
    while game_state(board) == 2:
        # The game has started

        if whose_turn(turn_num) == 1:
            player_current = player_1
        else:
            player_current = player_2

        print_board(board)
        print()

        move = get_move(board)
        board = insert_move(move, board, player_current)
        turn_num += 1

        # Visually separates subsequent moves
        print()

    print()
    print_board(board)

    result = game_state(board)
    if result == 0:
        print('Player X won!')
    elif result == 1:
        print('Player O won!')
    else:
        print('The game was a draw!')


if __name__ == '__main__':
    main()
