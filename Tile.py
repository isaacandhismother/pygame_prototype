import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, image, minable, time_to_mine=0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img = image
        self.row = x // tile_size[0]
        self.column = y // tile_size[1]
        self.width = width
        self.height = height
        self.selected = False
        self.mining = False
        self.minable = minable
        self.time_to_mine = time_to_mine * fps  # How many frames to break
        self.mining_progression = 0
        self.pos_on_screen = None
        self.hitbox = None

    def __repr__(self):
        return f'<Object Tile>'

    def draw(self, sc, x, y):
        try:
            self.image = pygame.image.load(self.img)
            self.image = pygame.transform.scale(self.image, (tile_size[0], tile_size[1]))
        except FileNotFoundError:
            self.image = pygame.Surface((tile_size[0], tile_size[1]))
            self.image.fill('black')

        self.hitbox = pygame.Surface((self.width, self.height))
        self.hitbox.set_alpha(0)
        hitbox_rect = self.hitbox.get_rect(center=(x, y))

        rect = self.image.get_rect(center=(x, y))
        self.image.set_alpha(255)

        if self.selected:
            self.image.set_alpha(220)

        sc.blit(self.hitbox, hitbox_rect)
        sc.blit(self.image, rect)

        self.selected = False

    def update(self):
        self.image.set_alpha(255)
        if self.selected:
            self.image.set_alpha(200)

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        top_left = self.pos_on_screen[0] - self.width / 2
        top_right = self.pos_on_screen[0] + self.width / 2
        bottom_left = self.pos_on_screen[1] - self.height / 2
        bottom_right = self.pos_on_screen[1] + self.height / 2

        if top_left < mouse_pos[0] < top_right and bottom_left < mouse_pos[1] < bottom_right:
            return True
        return False
