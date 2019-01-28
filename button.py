'''
Created on Jan 22, 2019

@author: RayL
'''
from sprites import button #Import button sprite

class Button():
    """Class to Represent Buttons on the Main Menu"""
    
    def __init__(self,text,window,x,y,decision):
        """Constructor"""
        self.text = text #Text on the Button
        self.window = window #Pygame Window
        self.x = x
        self.y = y 
        self.decision = decision #Decision that the button returns (for main menu navigation)
        
    def draw(self):
        """Draw the button"""
        self.window.blit(button,(self.x,self.y)) #Draw button sprite
        self.window.blit(self.text,(self.x + 40,self.y + 20)) #Draw text on button
    
    def getDecision(self):
        """Return the decision the button holds"""
        return self.decision