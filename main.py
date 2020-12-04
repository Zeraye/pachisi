import pygame
from events import check_events
from draw import draw
from constants import WIDTH, HEIGHT, FPS
from functions import start_game, play_turn, next_turn
from variables import turn

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pachisi")

def main(screen):
    clock = pygame.time.Clock()
    start_game()
    while True:
        clock.tick(FPS)
        check_events(pygame.event.get())
        play_turn()
        next_turn()
        draw(screen)

if __name__ == '__main__':
    main(WINDOW)
