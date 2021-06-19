import pygame
import constants
import variables

def draw_grid(screen):
    w = constants.WIDTH / 15
    h = constants.HEIGHT / 15
    for i in range(15):
        pygame.draw.line(screen, constants.BLACK,
                         (i*w, 0), (i*w, constants.HEIGHT))
    for i in range(15):
        pygame.draw.line(screen, constants.BLACK,
                         (0, i*h), (constants.WIDTH, i*h))

def draw_bases_big(screen):
    w = constants.WIDTH / 15
    h = constants.HEIGHT / 15
    # red base
    pygame.draw.rect(screen, constants.ORANGE,
                     pygame.Rect((0, 0), (6*w, 6*h)))
    # green base
    pygame.draw.rect(screen, constants.ORANGE,
                     pygame.Rect((9*w, 0), (6*w, 6*h)))
    # yellow base
    pygame.draw.rect(screen, constants.ORANGE,
                     pygame.Rect((0, 9*w), (6*w, 6*h)))
    # blue base
    pygame.draw.rect(screen, constants.ORANGE,
                     pygame.Rect((9*w, 9*w), (6*w, 6*h)))

def draw_bases_small(screen):
    w = constants.WIDTH / 15
    h = constants.HEIGHT / 15
    # red base
    pygame.draw.rect(screen, constants.RED,
                     pygame.Rect((w, h), (w, h)))
    pygame.draw.rect(screen, constants.RED,
                     pygame.Rect((4*w, h), (w, h)))
    pygame.draw.rect(screen, constants.RED,
                     pygame.Rect((w, 4*h), (w, h)))
    pygame.draw.rect(screen, constants.RED,
                     pygame.Rect((4*w, 4*h), (w, h)))
    # green base
    pygame.draw.rect(screen, constants.GREEN,
                     pygame.Rect((10*w, h), (w, h)))
    pygame.draw.rect(screen, constants.GREEN,
                     pygame.Rect((13*w, h), (w, h)))
    pygame.draw.rect(screen, constants.GREEN,
                     pygame.Rect((10*w, 4*h), (w, h)))
    pygame.draw.rect(screen, constants.GREEN,
                     pygame.Rect((13*w, 4*h), (w, h)))
    # yellow base
    pygame.draw.rect(screen, constants.YELLOW,
                     pygame.Rect((10*w, 10*h), (w, h)))
    pygame.draw.rect(screen, constants.YELLOW,
                     pygame.Rect((13*w, 10*h), (w, h)))
    pygame.draw.rect(screen, constants.YELLOW,
                     pygame.Rect((10*w, 13*h), (w, h)))
    pygame.draw.rect(screen, constants.YELLOW,
                     pygame.Rect((13*w, 13*h), (w, h)))
    # blue base
    pygame.draw.rect(screen, constants.BLUE,
                     pygame.Rect((w, 10*h), (w, h)))
    pygame.draw.rect(screen, constants.BLUE,
                     pygame.Rect((4*w, 10*h), (w, h)))
    pygame.draw.rect(screen, constants.BLUE,
                     pygame.Rect((w, 13*h), (w, h)))
    pygame.draw.rect(screen, constants.BLUE,
                     pygame.Rect((4*w, 13*h), (w, h)))

def draw_middle(screen):
    w = constants.WIDTH / 15
    h = constants.HEIGHT / 15
    pygame.draw.rect(screen, constants.PURPLE,
                     pygame.Rect((6*w, 6*h), (3*w, 3*h)))

def draw_color_roads(screen):
    w = constants.WIDTH / 15
    h = constants.HEIGHT / 15
    # red road
    pygame.draw.rect(screen, constants.RED,
                     pygame.Rect((w, 7*h), (5*w, h)))
    pygame.draw.rect(screen, constants.RED,
                     pygame.Rect((w, 6*h), (w, h)))
    # green road
    pygame.draw.rect(screen, constants.GREEN,
                     pygame.Rect((7*w, h), (w, 5*h)))
    pygame.draw.rect(screen, constants.GREEN,
                     pygame.Rect((8*w, h), (w, h)))
    # yellow road
    pygame.draw.rect(screen, constants.YELLOW,
                     pygame.Rect((9*w, 7*h), (5*w, h)))
    pygame.draw.rect(screen, constants.YELLOW,
                     pygame.Rect((13*w, 8*h), (w, h)))
    # blue road
    pygame.draw.rect(screen, constants.BLUE,
                     pygame.Rect((7*w, 9*h), (w, 5*h)))
    pygame.draw.rect(screen, constants.BLUE,
                     pygame.Rect((6*w, 13*h), (w, h)))

def draw_pawns(screen):
    for pawn in variables.pawns:
        pawn.draw(screen)

def draw_main(screen):
    screen.fill(constants.WHITE)
    draw_bases_big(screen)
    draw_bases_small(screen)
    draw_middle(screen)
    draw_color_roads(screen)
    draw_pawns(screen)
    draw_grid(screen)
    pygame.display.flip()
