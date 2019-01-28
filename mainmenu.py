'''
Created on Jan 22, 2019

@author: RayL
'''
from cursor import Cursor
from button import Button
import pygame
from sprites import bg
class Mainmenu():
    
    def __init__(self,window):
        self.window = window
        pygame.font.init()
        self.buttonFont = pygame.font.Font("emulogic.ttf",15)
        self.tutorialFont = pygame.font.Font("emulogic.ttf",10)
        self.playButton = Button(self.buttonFont.render("Play Game (2P)",
                                                        False,
                                                        (0,0,0)),
                                                        self.window,
                                                        400,
                                                        150,
                                                        1)
        self.tutorialButton = Button(self.buttonFont.render("Read Tutorial",
                                                            False,
                                                            (0,0,0)),
                                                            self.window,
                                                            400,
                                                            300,
                                                            2)     
           
        self.buttons = [self.playButton,self.tutorialButton]
        self.buttonIndex = 0
        self.cursor = Cursor(self.buttons[self.buttonIndex].x + 256,
                             self.buttons[self.buttonIndex].y,
                             self.window)
        self.running = True
        
    def moveCursor(self):
        self.cursor.move(self.buttons[self.buttonIndex].y)
    
    def draw(self):
        self.window.blit(bg,(0,0))
        self.playButton.draw()
        self.tutorialButton.draw()
        self.cursor.draw()
        pygame.display.update()
        
    def play(self):
        while self.running:
            pygame.time.delay(125)
            self.moveCursor()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 3
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                if self.buttonIndex + 1 == len(self.buttons):
                    self.buttonIndex = 0
                else:
                    self.buttonIndex += 1
            if keys[pygame.K_UP]:
                if self.buttonIndex - 1 == -1:
                    self.buttonIndex = len(self.buttons) - 1
                else:
                    self.buttonIndex -= 1
            if keys[pygame.K_RETURN]:
                return self.buttons[self.buttonIndex].getDecision()
            self.draw()    
    
    def tutorial(self):
        run = True
        texts = [self.tutorialFont.render("There are two players in this game.",False,(0,0,0)),
        self.tutorialFont.render("Player one is on the left and player two is on the right.",False,(0,0,0)),
        self.tutorialFont.render(" Player one uses WASD to move and space to shoot.", False, (0,0,0)),
        self.tutorialFont.render("Player two uses IJKL and Backslash (the button above enter) to shoot.",False,(0,0,0)),
        self.tutorialFont.render("Both players cannot cross the middle of the arena.",False,(0,0,0)),
        self.tutorialFont.render("Good luck and Have Fun! Press",False,(0,0,0)),
        self.tutorialFont.render("Enter to go back to the main menu.",False,(0,0,0))
        ]
        self.window.blit(bg,(0,0))
        i = 0
        for text in texts:
            self.window.blit(text,(200,i))
            i += 30
        pygame.display.update()
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                run = False
            print('Hello')