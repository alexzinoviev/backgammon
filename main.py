import random


BOARD_SIZE = 24
HALF_BOARD = 12
CHECKERS_QTY = 15
WHITE_CHECKER = 'w'
BLACK_CHECKER = 'b'


def get_score():
    return random.randint(1, 6)


def print_score():
    print(get_score())


def input_player_name(number):
    return input("What is the " + number + " player name?\n")


def check_players():
    while True:
        if players[1] == players[0]:
            print('name already exist')
            players[1] = input_player_name('second')
        else:
            print(players[get_first_turn()])
            break
"""
def create_board():
    return [" _ "] * BOARD_SIZE


def init_board(board):
    board[BOARD_SIZE - 1] = str(CHECKERS_QTY) + WHITE_CHECKER
    board[HALF_BOARD - 1] = str(CHECKERS_QTY) + BLACK_CHECKER


def print_board(board):
    for index in range(HALF_BOARD + 1, BOARD_SIZE + 1):
        print('{0:3d}'.format(index), end='')
    print('')

    for element in board[HALF_BOARD:]:
        print('{0:3s}'.format(element), end='')
    print('\n\n\n')

    for element in board[HALF_BOARD - 1::-1]:
        print('{0:3s}'.format(element), end='')
    print('')

    for index in range(HALF_BOARD, 0, -1):
        print('{0:3d}'.format(index), end=''),
    print('\n')
"""

def create_alt_board():

    alt_board = [[i+1," "," "]for i in range(BOARD_SIZE)]
    alt_board = alt_board[::-1]
    return alt_board



def init_alt_board(alt_board):

    alt_board[0][1] = CHECKERS_QTY
    alt_board[0][2] = WHITE_CHECKER
    alt_board[12][1] = CHECKERS_QTY
    alt_board[12][2] = BLACK_CHECKER

def print_alt_first_half_board(alt_board):

    """
    Visualize first half of the board
    """

    i = HALF_BOARD

    while i < BOARD_SIZE:
        print('{0:4d}'.format(alt_board[::-1][i][0]), end=" ")
        i += 1
    print('\n')

    i = HALF_BOARD   # It is unclear why we should initialize i again
    print(" ", end= " ")

    while i < BOARD_SIZE:
        if alt_board[::-1][i][1] != " ":
            print('{0:4s}'.format(str(alt_board[::-1][i][1]) + alt_board[::-1][i][2]), end=" ")
        else:
            print('{0:4s}'.format('_'), end=' ')
        i += 1

    print("\n\n\n")

def print_alt_second_half_board(alt_board):
    """
    Visualize second half of the board
    """

    i = HALF_BOARD

    print(" ", end= " ")
    while i < BOARD_SIZE:
        if alt_board[i][1] != " ":
            print('{0:4s}'.format(str(alt_board[i][1]) + alt_board[i][2]), end=" ")

        else:
            print('{0:4s}'.format('_'), end=' ')
        i += 1

    print('\n')

    i = HALF_BOARD # ????

    while i < BOARD_SIZE:
        print('{0:4d}'.format(alt_board[i][0]), end=" ")
        i += 1
    print('\n')


def get_first_turn():
    while True:
        player_1_score = get_score()
        player_2_score = get_score()
        if player_1_score != player_2_score:
            break
    if player_1_score > player_2_score:
        return 0
    else:
        return 1


#print_score()
#print_score()
#board = create_board()
#init_board(board)

alt_board = create_alt_board()
init_alt_board(alt_board)
print_alt_first_half_board(alt_board)
print_alt_second_half_board(alt_board)

players = [input_player_name('first'), input_player_name('second')]
check_players()

#print_board(board)


def get_dice_result():

    dice_results = []
    roll = 0
    NUMBER_OF_ROLLS = 2

    while roll < NUMBER_OF_ROLLS:
        dice_results.append(get_score())
        roll += 1

    if dice_results[0] == dice_results[1]:
        dice_results = dice_results * 2

    return dice_results

print(players[get_first_turn()])
print(get_dice_result())