'''
Created on Jan 7, 2019

@author: RayL
'''
from playerone import Playerone
from sprites import player_one_sprite
class Game():
    
    def __init__(self,window):
        self.window = window
        playerone = Playerone(0,0,5,(5,5),self.window,player_one_sprite)
    
    def draw(self):
        pass
    
    def play(self):
        pass