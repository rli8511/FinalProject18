'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from normalprojectile import Normal_Projectile
class Person():
    def __init__(self,x,y,size,spd,boundary,window,image,direction):
        self.spd = spd
        self.x = x 
        self.y = y
        self.boundary = boundary
        self.window = window
        self.size = size
        self.image = image
        self.hitbox = (self.x,self.y,self.size[0],self.size[1])
        self.direction = direction
        self.projectiles = []
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
            print(self.size[1]/2)
            self.projectiles.append(Normal_Projectile(self.x + self.size[0],
                                          self.y,
                                          10,
                                          self.direction,
                                          self.window,
                                          5))
        
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))