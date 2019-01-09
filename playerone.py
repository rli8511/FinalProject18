'''
Created on Jan 3, 2019

@author: RayL
'''
from person import Person
class Playerone(Person):
        
    def __init__(self,x,y,spd,boundary,window,image):
        Person.__init__(self,x,y,spd,boundary,window,image)
    
        