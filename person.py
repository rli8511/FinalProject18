'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from normalprojectile import Normal_Projectile
class Person():
    def __init__(self,x,y,spd,boundary,window,image,direction):
        self.spd = spd
        self.x = x 
        self.y = y
        self.boundary = boundary
        self.window = window
        self.image = image
        self.size = (image.get_width(),image.get_height())
        self.hitbox = (self.x,self.y,self.size[0],self.size[1])
        self.direction = direction
        self.projectiles = []
        self.isJump = False
        self.jumpStrength = 5
        self.jumpCount = self.jumpStrength
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x >= self.spd:
            self.x-= self.spd
        if keys[pygame.K_RIGHT] and self.x + 16 < self.boundary[0]:
            self.x+= self.spd
        if keys[pygame.K_UP] and not self.isJump:
            self.isJump = True
        if self.isJump:
            neg = 1
            if self.jumpCount >= -self.jumpStrength:
                if self.jumpCount < 0:
                    neg = -1
                self.y -= neg*(self.jumpCount ** 2)
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = self.jumpStrength
        if keys[pygame.K_DOWN] and self.y + 16 < self.boundary[1]:
            self.y += self.spd
        if keys[pygame.K_SPACE]:
            self.projectiles.append(Normal_Projectile(self.x + self.size[0],
                                          self.y + self.size[1]//2,
                                          10,
                                          self.direction,
                                          self.window,
                                          5))
        
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))