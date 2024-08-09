import easygui
"""Module providing a function to draw menu."""
import pygame_menu

from game.game import hunt_game_start
from game.save import save_high_score,load_high_score

def draw_menu(surface, menu_name):
    """Function sets theme of menu."""
    my_theme = pygame_menu.themes.THEME_DARK.copy()
    # mytheme.title_background_color=(0, 0, 0)
    myimage = pygame_menu.baseimage.BaseImage(
        image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_GRAY_LINES,
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
        # offset=(0,0)
    )
    my_theme.background_color = myimage
    # mytheme.Theme.title_bar_style.MENUBAR_STYLE_UNDERLINE_TITLE
    menu = pygame_menu.Menu(
        menu_name, surface.get_width(), surface.get_height(), theme=my_theme
    )

    return menu




def main_menu_screen(surface,score):
    """Function draws main menu."""
    menu = draw_menu(surface=surface, menu_name="Main Menu")
    high_score=score

    def start_the_game():
        """Function starts game."""
        hunt_game_start(surface)
        
    def save_game():
        save_high_score(score)
   
    def load_game():
        """Function load game from json file."""
        global high_score
        high_score=load_high_score()
        easygui.msgbox(f'Your corrent high score {high_score}', title="Loaded Save File")
               
        # menu.mainloop(surface)
    
    menu.set_title("Main Menu")
    menu.add.label(f"Current high score : {high_score} ")
    menu.add.text_input("Player name : ")
    menu.add.vertical_margin(5)
    menu.add.button("Start Game", start_the_game)
    menu.add.button("Save", save_game)
    menu.add.button("Load", load_game)
    menu.add.button("Quit", pygame_menu.events.EXIT)

    menu.mainloop(surface)
