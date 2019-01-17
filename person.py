'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from normalprojectile import Normal_Projectile

class Person():
    def __init__(self,x,y,spd,boundary,window,character,direction,jumpStrength):
        self.spd = spd
        self.x = x 
        self.y = y
        self.boundary = boundary
        self.window = window
        self.character = character
        self.size = character.value["size"]
        self.hitbox = (self.x,self.y,self.size[0],self.size[1])
        self.direction = direction
        self.projectiles = []
        self.isJump = False
        self.jumpStrength = jumpStrength
        self.jumpCount = self.jumpStrength
        self.stopped = True
        self.falling = False
        self.fallCount = 0
        self.walkCount = 0
        self.moving = False
        self.shooting = False
        
    def move(self):
        x_change = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x >= self.spd:
            x_change = - self.spd
        if keys[pygame.K_d] and self.x + 16 < self.boundary[0]:
            x_change = self.spd
        if keys[pygame.K_w] and not self.isJump and self.stopped:
            self.isJump = True
            self.stopped = False
            self.moving = True
        if keys[pygame.K_s] and self.stopped and self.y + self.size[1] < self.boundary[1]:
            self.stopped = False
            self.falling = True
            self.moving = True
        if keys[pygame.K_SPACE]:
            self.projectiles.append(Normal_Projectile(self.x + self.size[0],
                                          self.y + self.size[1]//2,
                                          30,
                                          self.direction,
                                          self.window,
                                          5))
            self.shooting = True
        else:
            self.shooting = False
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
        if x_change == 0:
            self.moving = False
        else:
            self.moving = True
            self.x += x_change
            
    def draw(self):
        if self.moving:
            if self.shooting:
                self.window.blit(self.character.value["shootwalk"][self.walkCount],(self.x,self.y))
            else:
                self.window.blit(self.character.value["walk"][self.walkCount], (self.x,self.y))
            self.walkCount += 1
        elif not self.moving:
            if self.shooting:
                self.window.blit(self.character.value["shootidle"],(self.x,self.y))
            else:
                self.window.blit(self.character.value["idle"],(self.x,self.y))
        if self.walkCount == 9:
            self.walkCount = 0
            
        