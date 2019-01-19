'''
Created on Jan 7, 2019

@author: RayL
'''
from person import Person
from sprites import bg
import pygame
from direction import Direction
from platform import Platform
from sprites import platform
from characters import Characters
from controls import Controls

class Game():
    
    def __init__(self,window):
        self.window = window
        self.playerone = Person(0,
                                575-64,
                                20,
                                (500-64,575-64),
                                self.window,
                                Characters.megaman_right,
                                Direction.right,
                                8,
                                Controls.WASD)
        self.playertwo = Person(900,
                                575-64,
                                20,
                                (500,575-64),
                                self.window,
                                Characters.megaman_left,
                                Direction.left,
                                8,
                                Controls.OKLColon)
        self.platforms = [Platform(275,self.window,platform),
                          Platform(425,self.window,platform),
                          Platform(575,self.window,platform)]
        
    def draw(self):
        self.window.blit(bg,(0,0))
        for platform in self.platforms:
            platform.draw()
        self.playerone.draw()
        self.playertwo.draw()
        for projectile in self.playerone.projectiles:
            projectile.draw()
        for projectile in self.playertwo.projectiles:
            projectile.draw()
        pygame.display.update()
    
    def play(self):
        running = True
        while running: #Main loop
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.playerone.move()
            self.playertwo.move()
            for platform in self.platforms:
                platform.stop_person(self.playerone)
                platform.stop_person(self.playertwo)
            for projectile in self.playerone.projectiles:
                if projectile.x > projectile.boundary[0]:
                    self.playerone.projectiles.pop(self.playerone.projectiles.index(projectile))
                projectile.move()
            for projectile in self.playertwo.projectiles:
                if projectile.x < 0:
                    self.playertwo.projectiles.pop(self.playertwo.projectiles.index(projectile))
                projectile.move()
            self.draw()