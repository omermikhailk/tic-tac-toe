COORD_MAP = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }


def make_board():
    """
    Returns a tic tac toe board (consisting of 2D lists).
    """
    board = [[] for i in range(3)]
    for j in range(3):
        board[j] = ['.' for w in range(3)]
    
    return board


def print_board(board):
    """
    Prints out the board row by row
    """
    for row in board:
        print(*row)


def validate_move(coord_str, board):
    """
    Validates the move and makes sure that it is in the board
    and that that square is not already occupied.
    
    Also makes sure that the move is an integer.
    
    Returns True for a valid move.
    """
    if not coord_str.isdigit():
        return False
    
    coord = int(coord_str)
    if 1 <= coord <= 9:
        x, y = COORD_MAP[coord]
        if board[x][y] == '.':
            # Valid move
            return True
    return False


def insert_move(coord, whose_turn, board):
    """
    Places either X or O (depends on `whose_turn`) in
    the given coordinate. And then returns the new board.
    """
    
    x, y = COORD_MAP[coord]
    board[x][y] = whose_turn
    
    return board


def game_decision(board):
    """
    Evaluates what the current position on the board means:
    
    0 for X victory
    1 for O victory
    2 for draw
    3 for ongoing
    
    Checks diagonally, vertically and horizontally
    for matching moves.
    """
    decision = {
        'X': 0,
        'O': 1,
        'Draw': 2,
        'Ongoing': 3
    }
    
    # Checking to see if diagonal elements match and that no '.' (dots) match
    diag_victory = (
            (board[0][0] == board[1][1] == board[2][2] and
             board[1][1] in 'XO')
            or
            (board[2][0] == board[1][1] == board[0][2] and
                board[1][1] in 'XO')
    )
    if diag_victory:
        return decision[board[1][1]]
    
    # Checking to see if horizontal elements match and that no '.' (dots) match
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] in 'XO':
            return decision[board[i][0]]
    
    # Checking to see if vertical elements match and that no '.' (dots) match
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[i][0] in 'XO':
            return decision[board[0][i]]
    
    for row in board:
        if '.' in row:
            return decision['Ongoing']
    
    # If there aren't any matches or empty spaces, it's a draw
    return decision['Draw']


def choose():
    """
    Lets the player decide if they want to be
    X or O. And then returns that decision.
    """
    while True:
        decision = input('Would you like to be \'X\' or \'O\' (please write, ' +
                         'in capitals):\n')
        # Validation of response
        if decision not in 'XO' or len(decision) > 1:
            print('\nPlease enter a correct response.')
            # Loop restarts until a correct response is received
            continue
        return decision


def get_turn(turn_num):
    """
    Takes in the current number of turns and returns
    whether it is (player 1 or player 2)'s turn.
    
    Player 1 always goes first.
    """
    if turn_num % 2:
        return 1
    return 2


def main():
    print('Welcome to Tic, Tac, Toe! Let\'s get started with some rules!')
    print('The top left square of the board has a coordinate of 1, ',
          'while the bottom right square of the board has a coordinate ',
          'of 9.')
    print('The numbers from the board increase from left to right.')
    print('\nNow let\'s play!\n\n')
    
    # Sets up the players and the board
    player_1 = choose()
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    board = make_board()
    turn_num = 1
    
    # Visually separates the start of the game from the setup
    print()
    
    # While the game is not drawn or won by either side it will continue
    while not game_decision(board) in (0, 1, 2):
        # The game has started
    
        if get_turn(turn_num) == 1:
            player_current = player_1
        else:
            player_current = player_2
    
        print_board(board)
        print('\nMake your move!')
    
        # Infinite loop until we get a correct coordinate input
        while True:
            move = input('Enter the coordinate you want to place your marker ' +
                         'on: ')
    
            if not validate_move(move, board):
                print('\nPlease enter a valid coordinate.\n')
                continue
            # Converted to an integer for use in `insert_board`
            move = int(move)
            break
    
        board = insert_move(move, player_current, board)
        turn_num += 1
    
        # Visually separates subsequent moves
        print()
    
    # Sees which player wins
    result = game_decision(board)
    if result == 2:
        print('The game is a draw!')
    if (player_1, result) in [('X', 0), ('O', 1)]:
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')


if __name__ == '__main__':
    main()
