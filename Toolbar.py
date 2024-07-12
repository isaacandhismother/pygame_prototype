import pygame

from Cell import Cell


class Toolbar:
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_width = height - 2
        self.cell_height = height - 4
        self.max_items = 10
        self.selected = False
        self.items = []
        for item in range(self.max_items):
            self.items.append(Cell(self.cell_width, self.cell_height,
                                   self.x + (item * self.cell_width + item*2 + 2), self.y + 2))

    def __getitem__(self, item):
        return self.items[item]

    def __call__(self, *args, **kwargs):
        print(self.items)

    def add_item(self, cell, item, count):
        cell = self.items[cell - 1]

        cell.add_item(item, count)

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        top_left = self.x
        top_right = self.x + self.width
        bottom_left = self.y
        bottom_right = self.y + self.height

        if top_left < mouse_pos[0] < top_right and bottom_left < mouse_pos[1] < bottom_right:
            return True
        return False

    def draw(self, sc, x, y):
        surf = pygame.Surface((self.width, self.height))
        surf.fill('dimgray')
        rect = surf.get_rect(topleft=(x, y))
        sc.blit(surf, rect)
        for item in self.items:
            item.draw(sc, item.x, item.y)

    def update(self):
        pass
