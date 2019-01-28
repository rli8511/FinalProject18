'''
Created on Jan 22, 2019

@author: RayL
'''
from cursor import Cursor #Import needed sprites/ classes
from button import Button
import pygame
from sprites import bg

class Mainmenu():
    """Class that represents the main menu"""
    def __init__(self,window):
        """Constructor"""
        self.window = window 
        pygame.font.init()
        self.buttonFont = pygame.font.Font("emulogic.ttf",15) #Prepare fonts
        self.tutorialFont = pygame.font.Font("emulogic.ttf",10)
        self.titleFont = pygame.font.Font("emulogic.ttf",25)
        self.title = self.titleFont.render("Megaman Battles", False, (0,0,0))
        self.playButton = Button(self.buttonFont.render("Play Game (2P)",
                                                        False,
                                                        (0,0,0)),
                                                        self.window,
                                                        400,
                                                        150,
                                                        1) #Initialize player button
        self.tutorialButton = Button(self.buttonFont.render("Read Tutorial",
                                                            False,
                                                            (0,0,0)),
                                                            self.window,
                                                            400,
                                                            300,
                                                            2)     #Initialize tutorial button
        self.buttons = [self.playButton,self.tutorialButton] #List to hold buttons
        self.buttonIndex = 0 #Index to see which button is chosen.
        self.cursor = Cursor(self.buttons[self.buttonIndex].x + 256,
                             self.buttons[self.buttonIndex].y,
                             self.window) #Initialize cursor
        self.running = True
        
    def draw(self):
        """Draw main menu"""
        self.window.blit(bg,(0,0)) #Draw background first
        self.window.blit(self.title,(350,50)) #Draw title
        self.playButton.draw() #Draw buttons
        self.tutorialButton.draw()
        self.cursor.draw() #Draw cursor
        pygame.display.update() #Update display
        
    def run(self):
        """Run the main menu"""
        while self.running:
            pygame.time.delay(125) #Delay to not take multiple inputs at once
            self.cursor.move(self.buttons[self.buttonIndex].y) #Move the cursor
            for event in pygame.event.get(): #Loop to check for user exit. 
                    if event.type == pygame.QUIT:
                        return 3
            keys = pygame.key.get_pressed() #Get keys
            if keys[pygame.K_DOWN]: #If they pressed down
                if self.buttonIndex + 1 == len(self.buttons): #If the index exceeds the list length
                    self.buttonIndex = 0 #Move the cursor to the first button
                else:
                    self.buttonIndex += 1 #Move the cursor down.
            if keys[pygame.K_UP]: #If up is pressed
                if self.buttonIndex - 1 == -1: #If the index is less than 0
                    self.buttonIndex = len(self.buttons) - 1 #Move the cursor to the last button
                else:
                    self.buttonIndex -= 1 #Move the cursor up
            if keys[pygame.K_RETURN]: #If Enter is pressed
                return self.buttons[self.buttonIndex].getDecision() #Return decision stored in selected button
            self.draw() #Draw
    
    def tutorial(self):
        run = True
        texts = [self.tutorialFont.render("There are two players in this game.",False,(0,0,0)),
        self.tutorialFont.render("Player one is on the left and player two is on the right.",False,(0,0,0)),
        self.tutorialFont.render("Player one uses WASD to move and space to shoot.", False, (0,0,0)),
        self.tutorialFont.render("Player two uses IJKL and Backslash (the button above enter) to shoot.",False,(0,0,0)),
        self.tutorialFont.render("Both players cannot cross the middle of the arena.",False,(0,0,0)),
        self.tutorialFont.render("Good luck and Have Fun! Press",False,(0,0,0)),
        self.tutorialFont.render("Enter to go back to the main menu.",False,(0,0,0))
        ] #Tutorial text split into lines
        self.window.blit(bg,(0,0)) #Blit background once.
        i = 0
        for text in texts: #Blit each line of text
            self.window.blit(text,(200,i))
            i += 30
        pygame.display.update() #Update display
        while run: #Main loop
            pygame.time.delay(100) #Delay
            for event in pygame.event.get(): #Loop to check for user exit. 
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]: #If enter is pressed, exit
                run = False