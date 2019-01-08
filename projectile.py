'''
Created on Jan 7, 2019

@author: RayL
'''
import pygame

class Projectile():
    """Class that represents projectiles"""
    def __init__(self,x,y,spd,radius,direction,window):
        self.x = x
        self.y = y
        self.spd = spd
        self.radius = radius
        self.direction = direction
        self.window = window
    
    def draw(self):
        pygame.draw.circle(self.window,(0,0,0),(self.x,self.y),self.radius)
        
        