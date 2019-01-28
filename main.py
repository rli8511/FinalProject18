'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from game import Game
from mainmenu import Mainmenu
pygame.init() #Initialize pygame
window_x = 1000 #Window size
window_y = 600 
window = pygame.display.set_mode((window_x,window_y)) #Create window

game = Game(window)
menu = Mainmenu(window)
while True:
    decision = menu.play()
    if decision == 1:
        game.play()
        break
    elif decision == 2:
        menu.tutorial()
    elif decision == 3: 
        break
