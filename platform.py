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
        if (person.falling and
            person.y + person.size[1] >= self.y - person.jumpStrength**2 and
            person.y + person.size[1] < self.y):
            #If the person is falling and is in range of the platfrom
            person.falling = False #Person is not falling and is stopped
            person.stopped = True
            person.fallCount = 0   
            person.y = self.y - person.size[1] #The person's y is set to be on the platform.
    def draw(self):
        """Draw the platform"""
        self.window.blit(self.image,(0,self.y))