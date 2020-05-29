from player import Player
from board import Board


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
    print_intro()

    # Sets up the board, players and turn number
    board = Board()
    board.make_board()
    turn_num = 1

    player_1, player_2 = Player(), Player()
    player_1.choose_side()
    if player_1.side == 'X':
        player_2.side = 'O'
    else:
        player_2.side = 'X'

    # To visually separate the start of the game from the rules
    print()

    # While the game is ongoing (2)
    while board.game_state() == 2:
        # The game has started
        if Player.whose_turn(turn_num) == 1:
            current_player = player_1.side
        else:
            current_player = player_2.side

        print(board)
        print()

        move = board.get_move()
        board.insert_move(move, current_player)
        turn_num += 1

        # Visually separates subsequent moves
        print()

    print()
    print(board)

    result = board.game_state()
    if result == 0:
        print('Player X won!')
    elif result == 1:
        print('Player O won!')
    else:
        print('The game was a draw!')


if __name__ == '__main__':
    main()

