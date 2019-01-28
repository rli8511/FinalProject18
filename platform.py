'''
Created on Jan 15, 2019

@author: RayL
'''

class Platform():
    """Class for platforms"""
    
    def __init__(self,y,window,image):
        """Constructor"""
        self.y = y
        self.window = window
        self.image = image
        
    def stopPerson(self,person):
        """Prevent the person from falling through the platform"""
        if person.falling and person.y + person.size[1] >= self.y - person.jumpStrength**2 and person.y + person.size[1] < self.y:
            person.falling = False
            person.stopped = True
            person.fallCount = 0   
            person.y = self.y - person.size[1]
    def draw(self):
        """Draw the platform"""
        self.window.blit(self.image,(0,self.y))