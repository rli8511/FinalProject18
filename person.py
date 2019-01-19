'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from normalprojectile import Normal_Projectile
from direction import Direction
class Person():
    def __init__(self,x,y,spd,boundary,window,character,direction,jumpStrength,controls):
        self.spd = spd
        self.x = x 
        self.y = y
        self.controls = controls
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
        self.cooldown = 10
        self.coolcounter = self.cooldown
        self.cooling = False
    def move(self):
        x_change = 0
        if self.cooling:
            self.coolcounter -= 1
            if self.coolcounter == 0:
                self.coolcounter = self.cooldown
                self.cooling = False
        keys = pygame.key.get_pressed()
        if self.direction == Direction.right:
            if keys[self.controls.value["Left"]] and self.x >= self.spd:
                x_change -= self.spd
            if keys[self.controls.value["Right"]] and self.x + self.size[0] < self.boundary[0]:
                x_change += self.spd
        else:
            if keys[self.controls.value["Left"]] and self.x >= self.boundary[0]:
                x_change -= self.spd
            if keys[self.controls.value["Right"]] and self.x + self.size[0] < self.window.get_width():
                x_change += self.spd
        if keys[self.controls.value["Jump"]] and not self.isJump and self.stopped:
            self.isJump = True
            self.stopped = False
            self.moving = True
        if keys[self.controls.value["Fall"]] and self.stopped and self.y + self.size[1] < self.boundary[1]:
            self.stopped = False
            self.falling = True
            self.moving = True
        if keys[self.controls.value["Shoot"]]:
            if len(self.projectiles) < 7 and self.coolcounter == self.cooldown and not self.cooling:
                self.projectiles.append(Normal_Projectile(self.x + self.size[0],
                                              self.y + self.size[1]//2,
                                              30,
                                              self.direction,
                                              self.window,
                                              5))
                self.shooting = True
                self.cooling = True
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
        if self.isJump or self.falling: 
            if self.shooting:
                self.window.blit(self.character.value["jumpshoot"], (self.x,self.y))
            else:
                self.window.blit(self.character.value["jump"], (self.x,self.y))
        else:
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
            
        