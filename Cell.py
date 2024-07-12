import pygame
from items import Item


class Cell:
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell = {}
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill('white')
        self.selected = False

    def __repr__(self):
        return f'<Object Cell, {self.cell}>'

    def add_item(self, key: Item, value):
        try:
            cell = self.cell[key]
            if 0 < cell < 100:
                cell += value
        except KeyError:
            self.cell[key] = value

    def take_item(self):
        if self.is_empty():
            for key, value in self.cell.items():
                item = key
                count = value
            self.cell.pop(item, None)
            return item, count

    def is_empty(self):
        if len(self.cell) != 0:
            return False
        return True

    def draw(self, sc, x, y):
        rect = self.surf.get_rect(topleft=(x, y))
        sc.blit(self.surf, rect)
        self.selected = False

    def update(self):
        self.surf.fill('white')
        if self.selected:
            self.surf.fill('lightgrey')

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        top_left = self.x
        top_right = self.x + self.width
        bottom_left = self.y
        bottom_right = self.y + self.height

        if top_left < mouse_pos[0] < top_right and bottom_left < mouse_pos[1] < bottom_right:
            return True
        return False
