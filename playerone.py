'''
Created on Jan 3, 2019

@author: RayL
'''
from sprites import player_one_sprite
from person import Person
class Playerone(Person):
        
    def __init__(self,x,y,spd,boundary,window,image):
        Person.__init__(x,y,spd,boundary,window,image)
    
        