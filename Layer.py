import pygame.sprite

from Tile import Tile
from items import *
from Player import Player

from settings import *


class Layer:
    def __init__(self, size):
        self.size = size
        self.layer = [[] for _ in range(size[0])]

        for row in self.layer:
            for _ in range(size[1]):
                row.append([])

    def __repr__(self):
        return '<Object World>'

    def __call__(self):
        for row in self.layer:
            print(row)

    def __getitem__(self, item):
        return self.layer[item]

    def __len__(self):
        return len(self.layer)

    def append(self, item):
        self.__getitem__(item).append(item)

    def remove(self, item):
        try:
            self.__getitem__(item).remove(item)
        except ValueError:
            pass

    def place(self, x, y, item):
        row = x // tile_size[0]
        column = y // tile_size[1]
        item.row = row
        item.column = column
        self.layer[row][column].append(item)
