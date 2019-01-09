'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from direction import Direction
class Person():
    def __init__(self,x,y,spd,boundary,window,image):
        self.spd = spd
        self.x = x 
        self.y = y
        self.boundary = boundary
        self.window = window
        self.image = image
    def move(self):
        keys = pygame.key.get_pressed()
        x_change = 0 
        y_change = 0
        if keys[pygame.K_LEFT] and self.x >= self.spd:
            x_change -= self.spd
            y_change = 0
        if keys[pygame.K_RIGHT] and self.x + 16 < self.boundary[0]:
            x_change += self.spd
            y_change = 0
        if keys[pygame.K_UP] and self.y >= self.spd:
            y_change -= self.spd
            x_change = 0
        if keys[pygame.K_DOWN] and self.y + 16 < self.boundary[1]:
            y_change += self.spd
            x_change = 0
        self.x += x_change
        self.y += y_change
        if keys[pygame.K_SPACE]:
            pass
        
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))