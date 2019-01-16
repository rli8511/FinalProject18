'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from normalprojectile import Normal_Projectile
class Person():
    def __init__(self,x,y,spd,boundary,window,image,direction,jumpStrength):
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
        self.jumpStrength = jumpStrength
        self.jumpCount = self.jumpStrength
        self.stopped = True
        self.falling = False
        self.fallCount = 0
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x >= self.spd:
            self.x-= self.spd
        if keys[pygame.K_RIGHT] and self.x + 16 < self.boundary[0]:
            self.x+= self.spd
        if keys[pygame.K_UP] and not self.isJump and self.stopped:
            self.isJump = True
            self.stopped = False
        if keys[pygame.K_DOWN] and self.stopped and self.y + self.size[1] < self.boundary[1]:
            self.stopped = False
            self.falling = True
        if keys[pygame.K_SPACE]:
            self.projectiles.append(Normal_Projectile(self.x + self.size[0],
                                          self.y + self.size[1]//2,
                                          10,
                                          self.direction,
                                          self.window,
                                          5))
        if self.isJump and not self.stopped and not self.falling:
            if self.jumpCount > 0:
                self.y -= (self.jumpCount ** 2)
                self.jumpCount -= 1
            else:
                self.jumpCount = self.jumpStrength
                self.falling = True
                self.isJump = False
        if self.falling and not self.stopped:
            self.y += (self.fallCount**2)
            self.fallCount += 1 
        else:
            self.fallCount = 0
            self.falling = False
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))