'''
Created on Jan 16, 2019

@author: RayL
'''
from enum import Enum
from sprites import mega_walkright
from sprites import mega_idle_right
from sprites import mega_shootright
from sprites import mega_shootidle
class Characters(Enum):
    
    megaman = {"walk": mega_walkright,
               "idle": mega_idle_right,
               "shootwalk": mega_shootright,
               "shootidle":mega_shootidle,
               "size": (64,64)
               }
