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

def change_size(sprite,size):
    return pygame.transform.scale(sprite,(size))

def prepare_sprite(sprite,color,size,flip = False):
    """Take in a list of sprites and make their background transparent"""
    sprite.set_colorkey(color)
    if flip == True:
        return pygame.transform.flip(pygame.transform.scale(sprite,size),True,False)
    return pygame.transform.scale(sprite,size)

def prepare_sprites(sprites,color,size,flip = False):
    """Take in a list of sprites and make their background transparent"""
    t_sprites = []
    for sprite in sprites:
        sprite.set_colorkey(color)
        if flip:
            t_sprites.append(pygame.transform.flip(pygame.transform.scale(sprite,size),True,False))
        else:
            t_sprites.append(pygame.transform.scale(sprite,size))   
    return t_sprites


player_one_sprite = get_sprite(filename,(0,0,45,55))
player_one_sprite = prepare_sprite(player_one_sprite,(255,255,255),(32,32),True)
