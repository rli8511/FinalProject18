'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from sprites import player_one_sprite
from game import Game
pygame.init() #Initialize pygame
window_x = 500 #Window size
window_y = 500 
window = pygame.display.set_mode((window_x,window_y)) #Create window
game = Game(window)
running = True
while running: #Main loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    game.play()
    
        
