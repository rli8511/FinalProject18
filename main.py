'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame 
from game import Game #Import game and main menu classes
from mainmenu import Mainmenu
pygame.init() #Initialize pygame
window_x = 1000 #Window size
window_y = 600 
window = pygame.display.set_mode((window_x,window_y)) #Create window

game = Game(window) #Initialize game and mainmenu
menu = Mainmenu(window)

while True: #Main Loop
    decision = menu.run() #Runs menu and returns 1,2, or 3. (Play, tutorial, or exit)
    if decision == 1:
        game.play() #Play
        break
    elif decision == 2:
        menu.tutorial() #Tutorial
    elif decision == 3: 
        break #Exit
