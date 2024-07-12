import pygame

from settings import *
from engine import *
from Menu import *


# pygame stuff
background = pygame.Surface((WIDTH, HEIGHT))
background.fill('white')

running = True
clicked = False
action_ended = False
clock = pygame.time.Clock()

while running:
    sc.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if current_engine[0] is not None:
                current_savestate[0].save(current_engine[0])
            pygame.quit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    if current_engine[0] is not None:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            unpause_game(action_ended)
            action_ended = True
        else:
            action_ended = False

        current_engine[0].run_game()
    update_menu(sc, clicked)

    pygame.display.flip()
    clock.tick(fps)
