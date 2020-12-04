from pawn import Pawn
from variables import pawns, turn, win
from time import sleep
from constants import debug_mode
from random import randint

def is_any_on_board(player):
    for pawn in pawns:
        if pawn.get_color() == player and pawn.get_pos_place() == 'board':
            return True
    return False


def start_game():
    for color in ('red', 'green', 'blue', 'yellow'):
        for i in range(4):
            pawns.append(Pawn(color, i, 'base'))
    turn.extend([1, 0, 0, 0])
    win.extend([0, 0, 0, 0])
    if debug_mode == 1:
        print('[DEBUG_MODE] >> Game starting')

def play_turn():
    if turn[0] == 1:
        player = 'red'
    elif turn[1] == 1:
        player = 'green'
    elif turn[2] == 1:
        player = 'blue'
    elif turn[3] == 1:
        player = 'yellow'
    if debug_mode == 1:
        print(f"[DEBUG_MODE] >> {player}'s turn starting")

    score = randint(1, 6)
    if debug_mode == 1:
        print(f'[DEBUG_MODE] >> Score: {score}')

    if is_any_on_board(player):
        pass
    else:
        pass

    time.sleep(5)

def next_turn():
    def _closest_not_winner(_index):
        if _index == len(turn) - 1:
            for i in range(len(turn)):
                if turn[i] != 1:
                    return i
        else:
            for i in range(_index + 1, len(turn)):
                if turn[i] != 1:
                    return i
            for i in range(_index):
                if turn[i] != 1:
                    return i
        return -1

    for i in range(len(turn)):
        if turn[i] == 1:
            turn[i] = 0
            if _closest_not_winner(i) != -1:
                turn[_closest_not_winner(i)] = 1
            else:
                if debug_mode == 1:
                    print('[DEBUG_MODE] >> Game has ended')
            break
