import pygame 

from screens import main_menu,draw_menu

game_name="No Idea!"

pygame.init()
pygame.display.set_caption(game_name)
surface = pygame.display.set_mode((800, 600))

menu=draw_menu(surface=surface,menu_name=game_name)

main_menu(surface=surface,menu_name="Main Menu",menu=menu)


