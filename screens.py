 
import pygame_menu


def main_menu(surface,game_name):

    # def set_difficulty(value, difficulty):
    #     pass

    def start_the_game():
        pass

    menu = pygame_menu.Menu(game_name, surface.get_width(), surface.get_height(),
                        theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('Choose Name :', default='Player',)
    # menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2),('Hard', 3)], onchange=set_difficulty)
    menu.add.button('Start Game', start_the_game)
    menu.add.button('Save', start_the_game)
    menu.add.button('Load', start_the_game)

    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)