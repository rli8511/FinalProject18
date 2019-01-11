'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame
filename = "test_sprites.png"

def get_sprite(file,rect):
    """Get a sprite at a certain rectangle in the sprite sheet"""
    sheet = pygame.image.load(file)
    
    rect = pygame.Rect(rect)
    image = pygame.Surface(rect.size)
    image.blit(sheet,(0,0),rect)
    return image

def make_transparent(sprites,color):
    """Take in a list of sprites and make their background transparent"""
    t_sprites = []
    for sprite in sprites:
        sprite.set_colorkey(color)
        t_sprites.append(sprite)   
    return t_sprites

def change_size(sprite,size):
player_one_sprite = get_sprite(filename,(0,0,45,55))
player_one_sprite.set_colorkey((255,255,255))
pygame.transform.scale(player_one_sprite, (16,16))

