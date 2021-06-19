import pygame
import events
import draw
import constants
import functions

pygame.init()

WINDOW = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pachisi")

def main(screen):
    clock = pygame.time.Clock()
    functions.start_game()
    while True:
        clock.tick(constants.FPS)
        events.check_events(pygame.event.get())
        functions.play_turn()
        draw.draw_main(screen)

if __name__ == '__main__':
    main(WINDOW)
