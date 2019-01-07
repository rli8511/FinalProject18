'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from sprites import player_one_sprite
from playerone import Playerone
pygame.init() #Initialize pygame
window_x = 500 #Window size
window_y = 500 
window = pygame.display.set_mode((window_x,window_y)) #Create window
running = True
while running: #Main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.blit(player_one_sprite.convert(),(0,0))
    pygame.display.update()
    
        
