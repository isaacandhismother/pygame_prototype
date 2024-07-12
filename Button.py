import pygame

pygame.init()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, background_color, text_color, font_size):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.background_color = background_color
        self.default_background_color = background_color
        self.text_color = text_color
        self.hover = False
        self.active = False
        self.is_pressed = False
        self.clicked = False
        self.function = None
        self.args = ()
        self.menu = None
        self.menulist = None
        self.type = None

        self.font = pygame.font.Font(None, font_size)
        self.font_size = font_size

    def update(self, sc, clicked):
        pos = pygame.mouse.get_pos()
        self.background_color = self.default_background_color

        if self.type == 'savestate':
            savestate = self.args[0]
            if not savestate.empty:
                self.background_color = 'darkgreen'

        if (self.x - self.width/2 < pos[0] < self.x + self.width/2) and (self.y - self.height/2 < pos[1] < self.y + self.height/2):
            self.hover = True
            self.background_color = 'grey'
        else:
            self.hover = False

        if not self.hover and clicked:
            self.active = False
        if self.active:
            if self.hover and clicked:
                self.is_pressed = True
            elif not clicked and self.is_pressed and self.hover:
                self.is_pressed = False
                try:
                    self.function(*self.args)
                except TypeError:
                    pass
            else:
                self.is_pressed = False
        if not clicked:
            self.active = True

        surf = pygame.Surface((self.width, self.height))
        surf.fill(self.background_color)
        rect = surf.get_rect(center=(self.x, self.y))

        sc.blit(surf, rect)
        # Алгоритм рендеринга слов

        text = self.font.render(self.text, True, self.text_color)
        text_size = text.get_size()

        collection = [word.split(' ') for word in self.text.splitlines()]
        space = self.font.size(' ')[0]
        margin = self.width / 10
        x = self.x - text_size[0] / 2
        y = self.y - text_size[1] / 2
        for lines in collection:
            for words in lines:
                word_surface = self.font.render(words, True, self.text_color)
                word_width, word_height = word_surface.get_size()
                if x + word_width + margin > self.x + self.width/2:
                    x = self.x - word_width / 2
                    y += word_height
                sc.blit(word_surface, (x, y))
                x += word_width + space
            x = self.x - text_size[0] / 2
            y += word_height

    def set_function(self, *, function, args: tuple):
        self.function = function
        self.args = args
