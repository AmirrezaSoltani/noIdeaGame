import pygame_menu
import game
mytheme=None


def draw_menu(surface,menu_name):

    mytheme = pygame_menu.themes.THEME_DARK.copy()
    # mytheme.title_background_color=(0, 0, 0)
    myimage = pygame_menu.baseimage.BaseImage(
    image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_GRAY_LINES,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
    # offset=(0,0)
    )
    mytheme.background_color = myimage
    # mytheme.Theme.title_bar_style.MENUBAR_STYLE_UNDERLINE_TITLE
    menu = pygame_menu.Menu(menu_name, surface.get_width(), surface.get_height(),
                        theme=mytheme)

    return menu

def main_menu_screen(surface):
    menu =draw_menu(surface=surface,menu_name="Main Menu")

    def start_the_game():
        game.HuntGame(surface)
        # choose_mode_screen(menu=menu,surface=surface)
        pass
    menu.set_title("Main Menu")
    # menu.add.text_input('Choose Name :', default='Player',)
    
    menu.add.button('Start Game', start_the_game)
    menu.add.button('Save', start_the_game)
    menu.add.button('Load', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)
def choose_mode_screen(menu,surface):

    def start_the_game(type):
        
        pass
    menu.clear()
    # menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2),('Hard', 3)], onchange=set_difficulty)
    menu.set_title("Play Game")
    menu.add.label("Choose your playing mode: ")
    menu.add.vertical_margin(30)
    menu.add.button('Solo', start_the_game("Solo"))
    menu.add.button('2 Player', start_the_game("2 Player"))
    menu.mainloop(surface)
