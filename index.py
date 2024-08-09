import sys
import pygame
from game.screens import main_menu_screen

print(pygame.version)
print(sys.version)

GAME_NAME = "Hunt the Ducks!"

pygame.init()
pygame.display.set_caption(GAME_NAME)
surface = pygame.display.set_mode((800, 600))


main_menu_screen(surface=surface,score=0)
