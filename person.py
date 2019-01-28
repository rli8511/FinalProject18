'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from projectile import Projectile
from direction import Direction
class Person():
    """Class to represent a person"""
    def __init__(self,x,y,spd,boundary,window,character,direction,jumpStrength,controls,health):
        """Constructor"""
        self.spd = spd
        self.x = x 
        self.y = y
        self.controls = controls #Dictionary for controls
        self.boundary = boundary #Limits of the player
        self.window = window 
        self.character = character #Dictionary for character sprites and information
        self.size = character.value["size"] #Tuple in character dictionary
        self.direction = direction #Direction enum
        self.projectiles = []
        self.isJump = False #Bool that determines if the player is jumping
        self.jumpStrength = jumpStrength #Int that determines how high the player can jump
        self.jumpCount = self.jumpStrength #Int that determines where the player is in the jump
        self.stopped = True #Bool to determine if the player is stopped by a platform.
        self.falling = False #Bool that determines if the player is falling.
        self.fallCount = 0 #Int that determines how long the player is falling.
        self.walkCount = 0 #Int used to cycle sprites
        self.moving = False
        self.shooting = False
        self.cooldown = 18 #Time between each shot. 
        self.coolcounter = self.cooldown #Counter for cooldown
        self.cooling = False #Bool if the player cooling down?
        self.health = health 
        self.currenthealth = self.health
        self.isAlive = True
        
    def getHit(self,projectile):
        """Determines whether a given projectile hites the person."""
        if (projectile.x <= self.x + self.size[0] and #If the projectile is in the player's hitbox
            projectile.x >= self.x and 
            projectile.y >= self.y and 
            projectile.y <= self.y + self.size[1]):
            self.currenthealth -= 1 #Remove hp
            if self.currenthealth == 0: #If he is dead. 
                self.isAlive = False
            return True
        return False
    
    def move(self):
        """Function for player to move or shoot"""
        x_change = 0
        if self.cooling: #If cooling, lower cool counter.
            self.coolcounter -= 1
            if self.coolcounter == 0: #If he is cooled down, reset coolcounter and set cooling to false.
                self.coolcounter = self.cooldown 
                self.cooling = False
        keys = pygame.key.get_pressed()
        if self.direction == Direction.right: #If he is facing right:
            if keys[self.controls.value["Left"]] and self.x >= self.spd: #If left is pressed and player not at boundary
                x_change -= self.spd #Move left
            if keys[self.controls.value["Right"]] and self.x + self.size[0] < self.boundary[0]: #If right is pressed and player not at boundary
                x_change += self.spd #Move right
        else: #If he is facing left:
            if keys[self.controls.value["Left"]] and self.x >= self.boundary[0]: #Same logic but different boundaries.
                x_change -= self.spd
            if keys[self.controls.value["Right"]] and self.x + self.size[0] < self.window.get_width():
                x_change += self.spd
        if keys[self.controls.value["Jump"]] and not self.isJump and self.stopped: #If up is pressed and not jumping and person is stopped on a platform.
            self.isJump = True #Player is jumping
            self.stopped = False #Player is not stopped
            self.moving = True #Player is moving.
        if keys[self.controls.value["Fall"]] and self.stopped and self.y + self.size[1] < self.boundary[1]: #If down is pressed and person is stopped and player is not at the bottom of the screen
            self.stopped = False #Player is not stopped
            self.falling = True #Player is falling
            self.moving = True #Player is moving.
        if keys[self.controls.value["Shoot"]]: #If the shoot button is pressed. 
            if len(self.projectiles) < 7 and self.coolcounter == self.cooldown and not self.cooling: #If the projectile limit is not met and player is not cooling down.
                self.projectiles.append(Projectile(self.x + self.size[0],
                                              round(self.y) + self.size[1]//2,
                                              25,
                                              self.direction,
                                              self.window,
                                              8)) #Create a projectile 
                self.shooting = True #Player is shooting and cooling down.
                self.cooling = True
        else:
            self.shooting = False #Player cannot shoot at this time
        if self.isJump and not self.stopped and not self.falling: #If jumping
            if self.jumpCount > 0: #Move the character based on quadratic equation if player has not reached peak.
                self.y -= (self.jumpCount ** 2)
                self.jumpCount -= 0.5
            else:
                self.jumpCount = self.jumpStrength #Player resets and falls once it reaches the peak. 
                self.falling = True
                self.isJump = False
        if self.falling and not self.stopped: #If falling
            self.y += (self.fallCount**2) #Character falls based on quadratic equation 
            self.fallCount += 0.5
        else:
            self.fallCount = 0 #Reset fall.
            self.falling = False
        if x_change == 0: #If there is no change in x, person is not moving.
            self.moving = False
        else:
            self.moving = True #If there is a change in x, person is moving. move the person.
            self.x += x_change   
            
    def draw(self):
        """Draw the person."""
        if self.isJump or self.falling: #If the player is jumping or falling
            if self.shooting: #If the player is shooting
                self.window.blit(self.character.value["jumpshoot"], (self.x,self.y)) #Blit jumpshoot sprite
            else:
                self.window.blit(self.character.value["jump"], (self.x,self.y)) #Blit jump sprite
        else:
            if self.moving: #If the player is moving
                if self.shooting: #If the player is shooting
                    self.window.blit(self.character.value["shootwalk"][self.walkCount],(self.x,self.y)) #Blit shootwalk sprite
                else:
                    self.window.blit(self.character.value["walk"][self.walkCount], (self.x,self.y)) #Blit walk sprite
                self.walkCount += 1 #Increase walk count
            elif not self.moving: #Player is not moving
                if self.shooting: #If the player is moving
                    self.window.blit(self.character.value["shootidle"],(self.x,self.y)) #Blit shoot idle sprite
                else: 
                    self.window.blit(self.character.value["idle"],(self.x,self.y)) #Blit idle animation
        if self.walkCount == 9:
            self.walkCount = 0 #If sprite loop ends, reset it for walking animation.
        pygame.draw.rect(self.window,(255,0,0),(self.x,self.y - 8,self.size[0],8)) #Draw HP bar
        pygame.draw.rect(self.window,(0,255,0),
                         (self.x,self.y - 8,self.size[0] - (self.size[0]/self.health)*(self.health-self.currenthealth),
                          8))
            
        