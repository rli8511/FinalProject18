'''
Created on Jan 16, 2019

@author: RayL
'''
from enum import Enum 
import pygame

class Controls(Enum):
    """Enum Class for Control Schemes"""
    
    WASD = {"Right":pygame.K_d, 
              "Left":pygame.K_a,
              "Jump":pygame.K_w,
              "Fall":pygame.K_s,
              "Shoot":pygame.K_SPACE
              }
    
    OKLColon = {"Right":pygame.K_l,
              "Left":pygame.K_j,
              "Jump":pygame.K_i,
              "Fall":pygame.K_k,
              "Shoot":pygame.K_BACKSLASH
              }
