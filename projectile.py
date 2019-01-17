'''
Created on Jan 7, 2019

@author: RayL
'''
from direction import Direction
class Projectile():
    """Class that represents projectiles"""
    def __init__(self,x,y,spd,direction,window):
        self.x = x
        self.y = y
        self.spd = spd
        self.direction = direction
        self.window = window
        self.boundary = (self.window.get_width(),self.window.get_height())
    def move(self):
        """Move for a normal projectile"""
        if self.direction == Direction.right:
            self.x += self.spd 
        else:
            self.x -= self.spd
            

        
        