'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame
filename = "test_sprites.png"
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_sprite(file,rect):
    "Get a sprite at a certain rectangle in the sprite sheet"
    sheet = pygame.image.load(file)
    
    rect = pygame.Rect(rect)
    image = pygame.Surface(rect.size)
    image.blit(sheet,(0,0),rect)
    return image

player_one_sprite = get_sprite(filename,(0,0,44.6,55.2))
img=mpimg.imread(player_one_sprite)
imgplot = plt.imshow(img)
plt.show()
print(player_one_sprite)