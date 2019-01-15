'''
Created on Jan 11, 2019

@author: RayL
'''
import pygame
from projectile import Projectile
class Normal_Projectile(Projectile):
    
    def __init__(self,x,y,spd,direction,window,radius):
        Projectile.__init__(self,x,y,spd,direction,window)
        self.radius = radius
    def draw(self):
        pygame.draw.circle(self.window,(255,255,255),(self.x,self.y),self.radius)