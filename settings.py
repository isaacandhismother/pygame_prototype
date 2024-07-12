import pygame

fps = 60
WIDTH = 800
HEIGHT = 600
tile_size = (80, 80)
screen_center = WIDTH/2, HEIGHT/2
tiles_per_screen = WIDTH//tile_size[0], HEIGHT//tile_size[1]
sc = pygame.display.set_mode((WIDTH, HEIGHT))
