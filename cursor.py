'''
Created on Jan 22, 2019

@author: RayL
'''
from sprites import cursor #Import cursor sprite

class Cursor():
    """Class to represent cursor on the main menu"""
    
    def __init__(self,x,y,window):
        """Constructor"""
        self.x = x
        self.y = y
        self.window = window #Pygame window
        
    def draw(self):
        """Draw the cursor"""
        self.window.blit(cursor,(self.x,self.y))
    
    def move(self,y):
        """Move the cursor (only moves vertically)"""
        self.y = y
        