import json
import inspect
import os

from Tile import Tile
from settings import *


class SaveState:
    def __init__(self, folder):
        with open(f'{folder}/save_info.json', 'r') as file:
            data = json.load(file)
            for row in data:
                for key, value in row.items():
                    if key == 'empty':
                        empty = value
        self.empty = empty
        self.folder = folder

    def save(self, world):
        layers = world.layers
        # Save each tile in each layer
        for layer in range(len(layers)):
            with open(f'{self.folder}/layer{layer}.json', 'w', encoding='utf-8') as file:
                file.write('[\n')
                for tile in layers[layer]:
                    for element in tile:
                        for i in element:
                            variables = vars(i)
                            variables.pop('_Sprite__g', 'None')
                            variables.pop('image', None)
                            variables.pop('hitbox', None)
                            variables.pop('selected', None)
                            variables.pop('mining', None)
                            variables.pop('mining_progression', None)
                            variables.pop('pos_on_screen', None)
                            variables.pop('row', None)
                            variables.pop('column', None)
                            json.dump(variables, file)
                            file.write(',\n')

            with open(f'{self.folder}/layer{layer}.json', 'r') as file2:
                content = file2.read()

            with open(f'{self.folder}/layer{layer}.json', 'w') as file2:
                if len(content) > 2:
                    modified_content = content[:-2]
                    file2.write(modified_content)
                    file2.write('\n]')
                else:
                    file2.write(content)
                    file2.write('\n]')
            self.empty = False

        # Save savestate info
        with open(f'{self.folder}/save_info.json', 'w', encoding='utf-8') as file:
            file.write('[\n')
            world_info = {"empty": False}
            json.dump(world_info, file, indent=4)
            file.write('\n]')

        # Save world Info
        with open(f'{self.folder}/world_info.json', 'w', encoding='utf-8') as file:
            world_info = {"world_size": world.world_size,
                          "player_pos": [world.player.x, world.player.y]}
            json.dump(world_info, file, indent=4)

        print('Writing ended successfully!')

    def load_world(self, world):
        layers = world.layers
        for layer in range(len(layers)):
            with open(f'{self.folder}/layer{layer}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                for element in data:
                    obj = Tile(20, 20, 20, 20, 'sprites/dirt.png', False)

                    for key, value in element.items():
                        setattr(obj, key, value)
                    layers[layer].place(obj.x, obj.y, obj)

        world_info = self.load_world_info()
        for key, value in world_info.items():
            if key == 'player_pos':
                world.player.x = value[0]
                world.player.y = value[1]

    def load_world_info(self):
        with open(f'{self.folder}/world_info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def delete_savestate(self):
        if not self.empty:
            directory = 'G:/Pycharm projects/test(again)'

            os.remove(f'{directory}/{self.folder}/layer0.json')
            os.remove(f'{directory}/{self.folder}/layer1.json')
            os.remove(f'{directory}/{self.folder}/world_info.json')

            with open(f'{self.folder}/save_info.json', 'w', encoding='utf-8') as file:
                file.write('[\n')
                json.dump({"empty": True}, file)
                self.empty = True
                file.write('\n]')
