'''
Created on Jan 7, 2019

@author: RayL
'''
from person import Person #Import sprites and all other classes/enum classes
from sprites import bg
import pygame
from direction import Direction
from platform import Platform
from sprites import platform
from characters import Characters
from controls import Controls
from mainmenu import Mainmenu

class Game():
    """Game Class that puts all the entities of the game together."""
    
    def __init__(self,window):
        """Constructor"""
        self.window = window
        self.fps = 30
        
        #Initialize player one and player two. 
        self.playerone = Person(0,
                                575-64,
                                Characters.megaman_right.value["hp"],
                                (500-64,575-64),
                                self.window,
                                Characters.megaman_right,
                                Direction.right,
                                6,
                                Controls.WASD,
                                Characters.megaman_right.value["spd"]) 
        self.playertwo = Person(900,
                                575-64,
                                Characters.megaman_left.value["hp"],
                                (500,575-64),
                                self.window,
                                Characters.megaman_left,
                                Direction.left,
                                6,
                                Controls.OKLColon,
                                Characters.megaman_left.value["spd"])
        
        #Initialize platforms.
        self.platforms = [Platform(275,self.window,platform),
                          Platform(425,self.window,platform),
                          Platform(575,self.window,platform)]
    
        #Initialize clock
        self.clock = pygame.time.Clock()
        
        #Initialize menu
        self.menu = Mainmenu(self.window)
         
    def draw(self):
        """"Draw everything needed"""
        self.window.blit(bg,(0,0)) #Draw background first        
        for platform in self.platforms: #Draw all the platforms
            platform.draw()
        self.playerone.draw() #Draw players
        self.playertwo.draw()
        for projectile in self.playerone.projectiles: #Draw all projectiles
            projectile.draw()
        for projectile in self.playertwo.projectiles:
            projectile.draw() 
        pygame.display.update() #Update the display
    
    def play(self):
        """Run the Game"""
        running = True
        while running: #Main loop
            self.clock.tick(self.fps) #Update the clock by the fps every frame
            for event in pygame.event.get(): #Loop to check for user exit
                if event.type == pygame.QUIT:
                    running = False
            self.playerone.move() #Move players
            self.playertwo.move()
            for platform in self.platforms: #Check if each platform stops the player
                platform.stopPerson(self.playerone)
                platform.stopPerson(self.playertwo)
            for projectile in self.playerone.projectiles:
                if projectile.x > projectile.boundary[0]: #If the projectile is out the boundary, remove the projectile
                    self.playerone.projectiles.pop(self.playerone.projectiles.index(projectile))
                else:
                    if self.playertwo.getHit(projectile): #If playertwo is hit by player one, remove the projectile and hit the player
                        self.playerone.projectiles.pop(self.playerone.projectiles.index(projectile))
                        if not self.playertwo.isAlive: #If playertwo is dead.
                            running = False
                            print("Player one won.")
                    projectile.move() #Move the projectile
            for projectile in self.playertwo.projectiles: #Same loop for player two's projectiles
                if projectile.x < 0:
                    self.playertwo.projectiles.pop(self.playertwo.projectiles.index(projectile))
                else:
                    if self.playerone.getHit(projectile):
                        self.playertwo.projectiles.pop(self.playertwo.projectiles.index(projectile))
                        if not self.playerone.isAlive:
                            running = False
                            print("Player two won.")
                    projectile.move()
            self.draw() #Draw everything 
        