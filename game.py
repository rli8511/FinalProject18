'''
Created on Jan 7, 2019

@author: RayL
'''
from person import Person
from sprites import player_one_sprite
from sprites import bg
import pygame
from direction import Direction
from platform import Platform
from sprites import platform
class Game():
    
    def __init__(self,window):
        self.window = window
        self.playerone = Person(0,
                                475-player_one_sprite.get_height(),
                                10,
                                (600,475),
                                self.window,
                                player_one_sprite,
                                Direction.right,
                                8)
        self.platforms = [Platform(125,self.window,platform),
                          Platform(300,self.window,platform),
                          Platform(475,self.window,platform)]
    def draw(self):
        self.window.blit(bg,(0,0))
        for platform in self.platforms:
            platform.draw()
        self.playerone.draw()
        for projectile in self.playerone.projectiles:
            projectile.draw()
        pygame.display.update()
    
    def play(self):
        running = True
        while running: #Main loop
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for platform in self.platforms:
                platform.stop_person(self.playerone)
            self.playerone.move()
            self.draw()
            for projectile in self.playerone.projectiles:
                projectile.move()
            if self.playerone.stopped == False:
                print(self.playerone.stopped)