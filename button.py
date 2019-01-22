'''
Created on Jan 22, 2019

@author: RayL
'''
from sprites import button

class Button():
    
    def __init__(self,text,window,x,y,decision):
        self.text = text
        self.window = window
        self.x = x 
        self.y = y
        self.decision = decision
    def draw(self):
        self.window.blit(button,(self.x,self.y))
        self.window.blit(self.text,(self.x + 40,self.y + 20))