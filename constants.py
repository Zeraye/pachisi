# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (247, 165, 95)
PURPLE = (186, 85, 211)

# screen settings
WIDTH = 900
HEIGHT = 900

# game settings
FPS = 60

# development settings
debug_mode = 1

# drawing pawns
INDEX_BOARD = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
               (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0),
               (7, 0), (8, 0),
               (8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
               (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6),
               (14, 7), (14, 8),
               (13, 8), (12, 8), (11, 8), (10, 8), (9, 8),
               (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14),
               (7, 14), (6, 14),
               (6, 13), (6, 12), (6, 11), (6, 10), (6, 9),
               (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8),
               (0,7), (5, 6)]
INDEX_BASE = {"red":[(1, 1), (4, 1), (1, 4), (4, 4)],
              "green":[(10, 1), (13, 1), (10, 4), (13, 4)],
              "yellow":[(10, 10), (13, 10), (10, 13), (13, 13)],
              "blue":[(1, 10), (4, 10), (1, 13), (4, 13)]}
INDEX_WIN = {"red":[(1, 7), (2, 7), (3, 7), (4, 7), (5, 7)],
             "green":[(7, 1), (7, 2), (7, 3), (7, 4), (7, 5)],
             "yellow":[(13, 7), (12, 7), (11, 7), (10, 7), (9, 7)],
             "blue":[(7, 13), (7, 12), (7, 11), (7, 10), (7, 9)]}
