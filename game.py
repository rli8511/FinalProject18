'''
Created on Jan 7, 2019

@author: RayL
'''
from person import Person
from sprites import player_one_sprite
import pygame
from direction import Direction
class Game():
    
    def __init__(self,window):
        self.window = window
        self.playerone = Person(0,0,(16,16),5,(500,500),self.window,player_one_sprite,Direction.right)
    
    def draw(self):
        self.window.fill((0,0,0))
        self.window.blit(self.playerone.image,(self.playerone.x,self.playerone.y))
        for projectile in self.playerone.projectiles:
            projectile.draw()
        pygame.display.update()
    
    def play(self):
        running = True
        while running: #Main loop
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.playerone.move()
            self.draw()
            for projectile in self.playerone.projectiles:
                projectile.move()
            print(self.playerone.projectiles)