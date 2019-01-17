'''
Created on Jan 16, 2019

@author: RayL
'''
from enum import Enum
import pygame
class Controls(Enum):
    WASD = {"Right":pygame.K_d,
              "Left":pygame.K_a,
              "Jump":pygame.K_w,
              "Fall":pygame.K_s,
              "Shoot":pygame.K_SPACE
              }
    
    OKLColon = {"Right":pygame.K_SEMICOLON,
              "Left":pygame.K_k,
              "Jump":pygame.K_o,
              "Fall":pygame.K_l,
              "Shoot":pygame.K_RETURN   
              }

