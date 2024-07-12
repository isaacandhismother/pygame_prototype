import pygame.image


class Item:
    def __init__(self, height, width, icon):
        self.height = height
        self.width = width
        self.icon = icon

    def draw(self, sc, x, y):
        image = pygame.image.load(self.icon)
        image = pygame.transform.scale(image, (self.width, self.height))

        rect = image.get_rect(center=(x, y))

        sc.blit(image, rect)


class WoodTile(Item):
    def __init__(self, width, height, icon):
        super().__init__(width, height, icon)
