import pawn_class
import variables
import time
import constants
import random

def is_any_on_board(player):
    for pawn in variables.pawns:
        if pawn.get_color() == player and pawn.get_loc() == 'board':
            return True
    return False

def start_game():
    for color in ('red', 'green', 'blue', 'yellow'):
        for i in range(4):
            variables.pawns.append(pawn_class.Pawn(color, i, 'base'))
    if constants.debug_mode == 1:
        print('[DEBUG_MODE] >> Game starting')

def play_turn():
    if variables.turn['red'] == 1:
        variables.turn['red'] = 0
        player = 'green'
    elif variables.turn['green'] == 1:
        variables.turn['green'] = 0
        player = 'blue'
    elif variables.turn['blue'] == 1:
        variables.turn['blue'] = 0
        player = 'yellow'
    elif variables.turn['yellow'] == 1:
        variables.turn['yellow'] = 0
        player = 'red'
    variables.turn[player] = 1

    if constants.debug_mode == 1:
        print(f"[DEBUG_MODE] >> {player}'s turn starting")

    score = random.randint(5, 6)
    if constants.debug_mode == 1:
        print(f'[DEBUG_MODE] >> Score: {score}')

    if is_any_on_board(player):
        for pawn in variables.pawns:
            if pawn.get_color() == player and pawn.get_loc() != 'base':
                if constants.debug_mode == 1:
                    print(f'[DEBUG_MODE] >> Moving pawn')
                pawn.move(score)
                break
    else:
        if score == 6:
            for pawn in variables.pawns:
                if pawn.get_color() == player:
                    if constants.debug_mode == 1:
                        print(f'[DEBUG_MODE] >> Starting pawn')
                    pawn.start()
                    break

    time.sleep(1.5)

def manage_move(pawn, loc, index):
    for _pawn in variables.pawns:
        if _pawn.get_index() == index and _pawn.get_loc() == loc:
            if pawn.get_color() != _pawn.get_color():
                _pawn.set_index(0)
                _pawn.set_loc('base')
    pawn.set_index(index)
    pawn.set_loc(loc)
