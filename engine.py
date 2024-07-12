import pygame
import random
import json

from Ui_layer import UiLayer
from Inventory import Inventory
from Toolbar import Toolbar
from Cell import Cell
from items import *

from Player import Player
from Layer import Layer
from Tile import Tile

import world_generation
from settings import *

menuList = []
left_key_pressed = False


class Engine:
    def __init__(self, *, world_size: tuple):
        self.layers = []

        self.world_size = world_size

        # Creating an empty layers and filling them
        self.main_layer = Layer(self.world_size)
        self.layers.append(self.main_layer)

        self.objects_layer = Layer(self.world_size)
        self.layers.append(self.objects_layer)

        self.ui_layer = UiLayer()

        # Creating player
        self.player = Player(40, 80)
        self.player.x = self.main_layer.size[0] // 2 * tile_size[0]
        self.player.y = self.main_layer.size[1] // 2 * tile_size[1]
        self.player.row = self.main_layer.size[0] // 2
        self.player.column = self.main_layer.size[1] // 2

        self.inventory = Inventory(400, 300, 200, 150)
        self.inventory.add_item(1, 1, 'apple', 2)
        # inventory()

        self.toolbar_height = 60
        self.toolbar_width = (self.toolbar_height * 10) + 2
        self.toolbar = Toolbar(self.toolbar_width, self.toolbar_height, WIDTH // 2 - self.toolbar_width / 2,
                               HEIGHT - 70)
        self.toolbar.add_item(2, 'apple', 2)
        self.ui_layer.add_element(self.toolbar)

        # Printing layers
        # main_layer()
        # objects_layer()

    def generate_world(self):
        height = self.world_size[0]
        width = self.world_size[1]
        tiles = world_generation.generate_world(width, height, 13)

        for row in range(height):
            for column in range(width):
                surf = pygame.Surface((tile_size[0], tile_size[1]))
                rect = surf.get_rect(topleft=(row * tile_size[0], column * tile_size[1]))
                if tiles[row, column] == 'tree':
                    self.main_layer[row][column].append(Tile(tile_size[0],
                                                             tile_size[1],
                                                             row * tile_size[0],
                                                             column * tile_size[1],
                                                             image='sprites/grasstop.png',
                                                             minable=False))
                    self.objects_layer[row][column].append(Tile(30,
                                                                80,
                                                                row * tile_size[0],
                                                                column * tile_size[1],
                                                                image='sprites/flower_sprite.png',
                                                                minable=True))
                elif tiles[row, column] == 'water':
                    self.objects_layer[row][column].append(Tile(tile_size[0],
                                                                tile_size[1],
                                                                row * tile_size[0],
                                                                column * tile_size[1],
                                                                image='sprites/water_sprite.png',
                                                                minable=False))
                elif tiles[row, column] == 'ore':
                    self.main_layer[row][column].append(Tile(tile_size[0],
                                                             tile_size[1],
                                                             row * tile_size[0],
                                                             column * tile_size[1],
                                                             image='sprites/grasstop.png',
                                                             minable=False))
                    self.objects_layer[row][column].append(Tile(tile_size[0],
                                                                tile_size[1],
                                                                row * tile_size[0],
                                                                column * tile_size[1],
                                                                image='sprites/cobble_sprite.png',
                                                                minable=True))
                else:
                    self.main_layer[row][column].append(Tile(tile_size[0],
                                                             tile_size[1],
                                                             row * tile_size[0],
                                                             column * tile_size[1],
                                                             image='sprites/grasstop.png',
                                                             minable=False))

    def draw_world_layers(self, x, y, selected_object):
        # Iterating layers # # # #
        for layer in range(len(self.layers)):
            if 0 <= x < self.layers[layer].size[0] and 0 <= y < self.layers[layer].size[1]:
                tile = self.layers[layer][x][y]
                for obj in tile:
                    pos_on_screen = screen_center[0] + obj.x - self.player.x, screen_center[1] + obj.y - self.player.y
                    obj.pos_on_screen = pos_on_screen

                    if obj.is_hover():
                        selected_object = obj

                    obj.draw(sc, pos_on_screen[0], pos_on_screen[1])
        # # # # # # # # # # # # #

        self.player.row = self.player.x // tile_size[0]
        self.player.column = self.player.y // tile_size[1]

        self.player.draw(sc, screen_center[0], screen_center[1])

        return selected_object

    def update_layers(self, selected_object):
        global left_key_pressed
        mouse_press = pygame.mouse.get_pressed()
        # Updating selected object
        if selected_object is not None:
            try:
                selected_row, selected_column = selected_object.row, selected_object.column
            except AttributeError:
                selected_row, selected_column = 0, 0

            selected_object.selected = True

            # Placing on a selected tile
            if mouse_press[0]:
                if (len(self.objects_layer[selected_row][selected_column]) < 1 and
                        selected_object.__class__.__name__ == 'Tile'):
                    self.objects_layer.place(selected_row * tile_size[0],
                                             selected_column * tile_size[1],
                                             Tile(tile_size[0], tile_size[1],
                                                  selected_row * tile_size[0],
                                                  selected_column * tile_size[1],
                                                  image='sprites/dirt.png',
                                                  minable=True))
                if not left_key_pressed:
                    if (selected_object.__class__.__name__ == 'Cell' and
                            self.player.equiped_item is None and
                            not selected_object.is_empty()):
                        self.player.equiped_item = selected_object.take_item()
                        left_key_pressed = True
                        print(1)
                    elif (selected_object.__class__.__name__ == 'Cell' and
                          self.player.equiped_item is not None):
                        left_key_pressed = True
                        print(2)
            else:
                left_key_pressed = False

            # Mining a selected object
            if mouse_press[2]:
                if selected_object.__class__.__name__ == 'Tile':
                    if selected_object.minable:
                        self.player.mine(self.objects_layer, selected_object)
                    elif mouse_press[2] and not selected_object.selected:
                        selected_object.mining = False
                    else:
                        self.player.mining = False

    def draw_ui_layer(self):
        selected_object = None
        for element in self.ui_layer:
            if element.is_hover():
                selected_object = element
            for item in element:
                if item.is_hover():
                    selected_object = item
                item.update()

        return selected_object

    def run_game(self):
        first_tile = self.player.row - tiles_per_screen[0] // 2, self.player.column - tiles_per_screen[1] // 2
        selected_object = None

        if len(menuList) == 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.move_left()
                if self.player.x < 0:
                    self.player.x = 0
            elif keys[pygame.K_d]:
                self.player.move_right()
                if self.player.x > (self.main_layer.size[0] - 1) * tile_size[0]:
                    self.player.x = (self.main_layer.size[0] - 1) * tile_size[0]
            if keys[pygame.K_w]:
                self.player.move_up()
                if self.player.y < 0:
                    self.player.y = 0
            elif keys[pygame.K_s]:
                self.player.move_down()
                if self.player.y > (self.main_layer.size[1] - 1) * tile_size[1]:
                    self.player.y = (self.main_layer.size[1] - 1) * tile_size[1]

        for x in range(first_tile[0] - 1, first_tile[0] + tiles_per_screen[0] + 2):
            for y in range(first_tile[1] - 1, first_tile[1] + tiles_per_screen[1] + 2):
                selected_object = self.draw_world_layers(x, y, selected_object)

        selected_ui_element = self.draw_ui_layer()

        self.toolbar.draw(sc, self.toolbar.x, self.toolbar.y)

        if selected_ui_element is not None:
            selected_object = selected_ui_element

        if len(menuList) == 0:
            self.update_layers(selected_object)
