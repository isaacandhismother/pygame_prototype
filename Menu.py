import pygame

from engine import *
from Button import Button
from SaveState import SaveState

current_engine = [None]
current_savestate = [None]
game_paused = False


class Menu(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.background = None
        self.transparency = None
        self.background_type = None
        self.elements = []

    def add_background(self, background_type, background):
        self.background = background
        self.background_type = background_type

    def background_update(self, sc):
        if self.background_type == 'image':
            image = pygame.image.load(self.background).convert()
            rect = image.get_rect(topleft=(0, 0))
            sc.blit(image, rect)
        elif self.background_type == 'color':
            surf = pygame.Surface((self.width, self.height))
            surf.fill(self.background)
            if self.transparency is not None:
                surf.set_alpha(200)
            sc.blit(surf, (0, 0))

    def add(self, element):
        self.elements.append(element)

    def update(self, sc, clicked):
        self.background_update(sc)
        for currentElement in self.elements:
            currentElement.update(sc, clicked)


main_menu = Menu(800, 600)
choose_savestate_menu = Menu(800, 600)
create_world_menu = Menu(800, 600)
settings_menu = Menu(800, 600)
pause_menu = Menu(800, 600)


def add_menu(menu):
    menuList.append(menu)


def remove_menu():
    menuList.pop()


def unpause_game(action_status):
    global game_paused
    action_ended = action_status
    if not game_paused and not action_ended:
        try:
            menuList.index(pause_menu)
        except ValueError:
            add_menu(pause_menu)
            game_paused = True
    elif game_paused and not action_ended:
        try:
            remove_menu()
            game_paused = False
        except IndexError:
            pass


def exit_game():
    pygame.quit()


def quit_to_menu():
    unpause_game(False)
    current_savestate[0].save(current_engine[0])
    current_engine[0] = None
    add_menu(main_menu)


def clear_list(lst):
    lst.clear()


def create_world():
    clear_list(menuList)
    engine = Engine(world_size=(current_level_type, current_level_type))
    engine.generate_world()
    current_engine[0] = engine


def load_world():
    pass


def load_savestate_state(savestate, number):
    global current_savestate
    if savestate.empty:
        add_menu(create_world_menu)
    if not savestate.empty:
        clear_list(menuList)
        world_info = savestate.load_world_info()
        world_size = world_info['world_size']

        engine = Engine(world_size=(world_size[0], world_size[1]))

        savestate.load_world(engine)

        current_engine[0] = engine

    current_savestate[0] = savestate


levelTypes = [32, 64, 128, 256]
current_level_type = levelTypes[0]


def change_world_type(button):
    global current_level_type, levelTypes
    changed = False
    for i in range(len(levelTypes)):
        if current_level_type == levelTypes[i] and not changed:
            if i != len(levelTypes) - 1:
                current_level_type = levelTypes[i + 1]
            else:
                current_level_type = levelTypes[0]
            button.text = 'World type:  ' + str(current_level_type)
            changed = True


# -----Buttons----- #

play_button = Button(main_menu.width / 2, 220, 300, 50, 'Start campaign', 'black', 'white', 32)
play_button.set_function(function=add_menu, args=(choose_savestate_menu,))

# savestates and savestate buttons
savestate1 = SaveState('saves/save1')

savestate1_button = Button(150, 220, 100, 120, 'Save \n1', 'black', 'white', 32)
savestate1_button.type = 'savestate'
savestate1_button.set_function(function=load_savestate_state, args=(savestate1, 1))

delete_savestate1_button = Button(150, 320, 100, 50, 'Delete', 'black', 'white', 32)
delete_savestate1_button.set_function(function=savestate1.delete_savestate, args=())

savestate2 = SaveState('saves/save2')

savestate2_button = Button(350, 220, 100, 120, 'Save \n2', 'black', 'white', 32)
savestate2_button.type = 'savestate'
savestate2_button.set_function(function=load_savestate_state, args=(savestate2, 2))

delete_savestate2_button = Button(350, 320, 100, 50, 'Delete', 'black', 'white', 32)
delete_savestate2_button.set_function(function=savestate2.delete_savestate, args=())

savestate3 = SaveState('saves/save3')

savestate3_button = Button(550, 220, 100, 120, 'Save \n3', 'black', 'white', 32)
savestate3_button.type = 'savestate'
savestate3_button.set_function(function=load_savestate_state, args=(savestate3, ))

delete_savestate3_button = Button(550, 320, 100, 50, 'Delete', 'black', 'white', 32)
delete_savestate3_button.set_function(function=savestate3.delete_savestate, args=())

# # # #

world_type_button = Button(400, 320, 300, 50, 'World type:   ' + str(current_level_type), 'black', 'white', 32)
world_type_button.set_function(function=change_world_type, args=(world_type_button, ))

create_world_button = Button(170, 530, 220, 50, 'Create world', 'black', 'white', 32)
create_world_button.function = create_world

resume_button = Button(pause_menu.width / 2, 200, 200, 50, 'Resume', 'black', 'white', 32)

settings_button = Button(main_menu.width / 2, 320, 200, 50, 'Settings', 'black', 'white', 32)
settings_button.set_function(function=add_menu, args=(settings_menu, ))

quit_button = Button(main_menu.width / 2, 420, 200, 50, 'Quit', 'black', 'white', 32)
quit_button.set_function(function=exit_game, args=())

back_button = Button(650, 530, 200, 50, 'Back', 'black', 'white', 32)
back_button.set_function(function=remove_menu, args=())

graphics_button = Button(main_menu.width / 2, 400, 200, 50, 'Graphics', 'black', 'white', 32)

back_to_game_button = Button(pause_menu.width / 2, 280, 250, 45, 'Back to game', 'black', 'white', 28)
back_to_game_button.set_function(function=unpause_game, args=(False, ))

quit_to_menu_button = Button(pause_menu.width / 2, 350, 250, 45, 'Main menu', 'black', 'white', 28)
quit_to_menu_button.set_function(function=quit_to_menu, args=())

# -----Menus----- #

# Main menu

main_menu.add_background('color', 'dimgray')
main_menu.add(play_button)
main_menu.add(settings_button)
main_menu.add(quit_button)

# Play menu

choose_savestate_menu.add_background('color', 'lightblue')
choose_savestate_menu.add(savestate1_button)
choose_savestate_menu.add(delete_savestate1_button)
choose_savestate_menu.add(savestate2_button)
choose_savestate_menu.add(delete_savestate2_button)
choose_savestate_menu.add(savestate3_button)
choose_savestate_menu.add(delete_savestate3_button)
choose_savestate_menu.add(back_button)

# World creation menu

create_world_menu.add_background('color', 'pink')
create_world_menu.add(back_button)
create_world_menu.add(create_world_button)
create_world_menu.add(world_type_button)

# Settings menu

settings_menu.add_background('color', 'blue')
settings_menu.add(back_button)
settings_menu.add(graphics_button)

# Pause menu

pause_menu.add_background('color', 'black')
pause_menu.transparency = True
pause_menu.add(back_to_game_button)
pause_menu.add(quit_to_menu_button)

# -----Menu update-----#

menu_count = 0

add_menu(main_menu)


def update_menu(sc, clicked):
    # if menuList[len(menuList) - 1] == playMenu:
    #     if not savestate1.empty:
    #         savestate1.show_name(sc, 150, 20, 'black', 22)
    if menuList and len(menuList) != 0:
        menuList[len(menuList) - 1].update(sc, clicked)
