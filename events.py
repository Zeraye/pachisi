import pygame
def check_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
