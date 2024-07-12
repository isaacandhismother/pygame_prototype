import pygame


class UiLayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ui_layer = []

    def __getitem__(self, item):
        return self.ui_layer[item]

    def add_element(self, item):
        try:
            self.ui_layer.index(item)
        except ValueError:
            self.ui_layer.append(item)

    def remove_element(self, item):
        try:
            self.ui_layer.index(item)
        except ValueError:
            return None
        self.ui_layer.remove(item)

    def draw(self, item):
        self.ui_layer[item].draw()

    def update(self, item):
        self.ui_layer[item].update()
