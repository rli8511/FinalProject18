'''
Created on Jan 16, 2019

@author: RayL
'''
from enum import Enum 
from sprites import mega_sprites_right #Import megaman sprites (player one)
from sprites import mega_sprites_left #Import megaman sprites (Player two)

class Characters(Enum):
    """Enum Class for character sprites and details"""
    
    megaman_right = {"walk": mega_sprites_right[0], #megaman_right and megaman_left
               "idle": mega_sprites_right[1],       #are dictionaries holding sprites
               "shootwalk": mega_sprites_right[2],  #and character related information.
               "shootidle":mega_sprites_right[3],
               "jump": mega_sprites_right[4],
               "jumpshoot": mega_sprites_right[5],
               "size": (64,64),
               "hp" : 10,
               "spd": 10
               }
    
    megaman_left = {"walk": mega_sprites_left[0],
                    "idle": mega_sprites_left[1],
                    "shootwalk": mega_sprites_left[2],
                    "shootidle": mega_sprites_left[3],
                    "jump": mega_sprites_left[4],
                    "jumpshoot": mega_sprites_left[5],
                    "size": (64,64),
                    "hp" : 10,
                    "spd": 10
                    }
