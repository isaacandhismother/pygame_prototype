import pygame

from Cell import Cell


class Inventory:
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_width = width // 10
        self.cell_height = width // 10
        self.color = 'dimgray'
        self.items = [[] for _ in range(8)]

        for row in range(8):
            for column in range(10):
                self.items[row].append(Cell(self.cell_width, self.cell_height,
                                            self.x + (column * self.cell_width + column * 2 + 2),
                                            self.y + (row * self.cell_height + row * 2 + 2)))

    def __call__(self, *args, **kwargs):
        for row in self.items:
            print(row)

    def get_cell(self, row, column):
        print(self.items[row][column])

    def add_item(self, row, column, item, count):
        cell = self.items[row - 1][column - 1]

        cell.add_item(item, count)

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        top_left = self.x - self.width / 2
        top_right = self.x + self.width / 2
        bottom_left = self.y - self.height / 2
        bottom_right = self.y + self.height / 2

        if top_left < mouse_pos[0] < top_right and bottom_left < mouse_pos[1] < bottom_right:
            return True
        return False

    def draw(self, sc, x, y):
        pass
