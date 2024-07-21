import pygame 

from screens import main_menu

game_name="No Idea!"

pygame.init()
pygame.display.set_caption(game_name)
surface = pygame.display.set_mode((800, 600))



main_menu(surface,"Main Menu")

