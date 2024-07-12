import pygame


class Player:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.row = 0
        self.column = 0
        self.speed = 4
        self.mining = False
        self.mining_progression = 0
        self.accelerate = 2
        self.equiped_item = None
        self.surf = pygame.Surface((width, height))
        self.surf.fill('black')

    def draw(self, sc, x, y):
        rect = self.surf.get_rect(center=(x, y))
        sc.blit(self.surf, rect)

    def move_left(self):
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_SHIFT:
            accelerate = self.accelerate
        else:
            accelerate = 0
        self.x -= self.speed + accelerate

    def move_right(self):
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_SHIFT:
            accelerate = self.accelerate
        else:
            accelerate = 0
        self.x += self.speed + accelerate

    def move_up(self):
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_SHIFT:
            accelerate = self.accelerate
        else:
            accelerate = 0
        self.y -= self.speed + accelerate

    def move_down(self):
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_SHIFT:
            accelerate = self.accelerate
        else:
            accelerate = 0
        self.y += self.speed + accelerate

    def equip(self, item):
        self.equiped_item = item

    def mine(self, layer, item):
        if self.mining is False:
            item.mining_progression = item.time_to_mine
            item.mining = True
            self.mining = True
        if self.mining is True and item.mining is False:
            item.mining_progression = item.time_to_mine
            item.mining = True
        if self.mining is True and item.mining is True:
            item.mining_progression -= 4
            print(item.mining_progression)
            if item.mining_progression <= 0:
                layer[item.row][item.column].remove(item)
                self.mining = False
                item.mining = False
