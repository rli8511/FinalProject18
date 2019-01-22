'''
Created on Jan 22, 2019

@author: RayL
'''
from sprites import cursor

class Cursor():
    
    def __init__(self,x,y,window):
        self.x = x
        self.y = y
        self.window = window
        
    def draw(self):
        self.window.blit(cursor,(self.x,self.y))
    
    def move(self,y):
        self.y = y
        