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
        self.playButton = Button(self.buttonFont.render("Play Game (2P)",
                                                        False,
                                                        (0,0,0)),
                                                        self.window,
                                                        400,
                                                        150)
        self.tutorialButton = Button(self.buttonFont.render("Read Tutorial",
                                                            False,
                                                            (0,0,0)),
                                                            self.window,
                                                            400,
                                                            300)     
           
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
            pygame.time.delay(100)
            self.moveCursor()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
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
                return self.buttons[self.buttonIndex].decision
            self.draw()    
