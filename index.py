import pygame 

from screens import main_menu_screen

game_name="Hunt the Ducks!"

pygame.init()
pygame.display.set_caption(game_name)
surface = pygame.display.set_mode((800, 600))



main_menu_screen(surface=surface)


