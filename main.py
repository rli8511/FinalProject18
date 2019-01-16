'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from game import Game
pygame.init() #Initialize pygame
window_x = 600 #Window size
window_y = 500 
window = pygame.display.set_mode((window_x,window_y)) #Create window
game = Game(window)
game.play()
    
        
