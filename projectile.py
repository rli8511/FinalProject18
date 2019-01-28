'''
Created on Jan 7, 2019

@author: RayL
'''
from direction import Direction
import pygame

class Projectile():
    """Class that represents projectiles"""
    def __init__(self,x,y,spd,direction,window,radius):
        self.x = x
        self.y = y
        self.spd = spd
        self.direction = direction
        self.window = window
        self.boundary = (self.window.get_width(),self.window.get_height())
        self.radius = radius
    def move(self):
        """Move the projectile"""
        if self.direction == Direction.right:
            self.x += self.spd 
        else:
            self.x -= self.spd
            
    def draw(self):
        """Draw projectile"""
        pygame.draw.circle(self.window,(255,255,255),(self.x,self.y),self.radius)
            

        
        