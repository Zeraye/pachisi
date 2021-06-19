import pygame

def check_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            print((round(pygame.mouse.get_pos()[0]/60)),
                   round(pygame.mouse.get_pos()[1]/60))
