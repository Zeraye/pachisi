import variables
import functions
import constants
import pygame

class Pawn:

    def __init__(self, color, index, loc):
        self.color = color
        self.index = index
        self.loc = loc

    def get_color(self):
        return self.color

    def get_index(self):
        return self.index

    def get_loc(self):
        return self.loc

    def set_index(self, _index):
        self.index = _index

    def set_loc(self, _loc):
        self.loc = _loc

    def draw(self, screen):
        w = constants.WIDTH / 15
        h = constants.HEIGHT / 15
        board = constants.INDEX_BOARD
        base = constants.INDEX_BASE
        win = constants.INDEX_WIN
        print(self.index%50)
        # ???????????????? chyba tak ale nie wiem
        self.index %= 50
        if self.loc == "board":
            pygame.draw.rect(screen, constants.BLACK,
                             pygame.Rect((board[self.index][0]*w+w/4, board[self.index][1]*h),
                                         (w/2, h)))
        elif self.loc == "base":
            pygame.draw.rect(screen, constants.BLACK,
                             pygame.Rect((base[self.color][self.index][0]*w+w/4, base[self.color][self.index][1]*h),
                                         (w/2, h)))
        else:
            pygame.draw.rect(screen, constants.BLACK,
                             pygame.Rect((win[self.color][self.index][0]*w+w/4, win[self.color][self.index][1]*h),
                                         (w/2, h)))

    def move(self, score):
        if self.loc == 'board':
            if constants.debug_mode == 1:
                print(f'[DEBUG_MODE] >> Moving {self.get_color()} in board')
            if self.color == 'red' and (self.index + score == 51 or
                                        self.index + score <= 4):
                if self.index + score == 51:
                    variables.win[player] += 1
                    self.delete()
                else:
                    functions.manage_move(self, 'win', self.index + score - 51)

            elif self.color == 'green' and 12 <= self.index + score <= 17:
                if self.index + score == 17:
                    variables.win[player] += 1
                    self.delete()
                else:
                    functions.manage_move(self, 'win', self.index + score - 12)

            elif self.color == 'yellow' and 25 <= self.index + score <= 30:
                if self.index + score == 30:
                    variables.win[player] += 1
                    self.delete()
                else:
                    functions.manage_move(self, 'win', self.index + score - 25)

            elif self.color == 'blue' and 38 <= self.index + score <= 43:
                if self.index + score == 43:
                    variables.win[player] += 1
                    self.delete()
                else:
                    functions.manage_move(self, 'win', self.index + score - 38)

            else:
                functions.manage_move(self, 'board', self.index + score)

        elif self.loc == 'win':
            if constants.debug_mode == 1:
                print(f'[DEBUG_MODE] >> Moving {self.get_color()} in win')
            if self.index + score >= 5:
                variables.win[player] += 1
                self.delete()
            else:
                functions.manage_move(self, 'win', self.index + score)

    def start(self):
        if constants.debug_mode == 1:
            print(f'[DEBUG_MODE] >> Starting {self.get_color()}')
        if self.get_color() == 'red':
            functions.manage_move(self, 'board', 0)
        elif self.get_color() == 'green':
            functions.manage_move(self, 'board', 13)
        elif self.get_color() == 'yellow':
            functions.manage_move(self, 'board', 26)
        elif self.get_color() == 'blue':
            functions.manage_move(self, 'board', 39)

    def delete(self):
        variables.pawns.remove(self)
        del self
