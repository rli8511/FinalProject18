'''
Created on Jan 7, 2019

@author: RayL
'''
from playerone import Playerone
from sprites import player_one_sprite
import pygame

class Game():
    
    def __init__(self,window):
        self.window = window
        self.playerone = Playerone(0,0,5,(500,500),self.window,player_one_sprite)
    
    def draw(self):
        pass
    
    def play(self):
        self.playerone.move()
        self.window.blit(self.playerone.image,(self.playerone.x,self.playerone.y))
        pygame.display.update()