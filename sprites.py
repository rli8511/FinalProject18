'''
Created on Jan 3, 2019

@author: RayL
'''
import pygame
filename = "test_sprites.png"
bg = "bg.png"
platform = "platform.png"
megaman = "megaman_sprites.png"
window = pygame.display.set_mode((1000,500))

def get_sprite(file,rect = None):
    """Get a sprite at a certain rectangle in the sprite sheet"""
    sheet = pygame.image.load(file)
    if rect is not None:
        rect = pygame.Rect(rect)
        image = pygame.Surface(rect.size)
        image.blit(sheet,(0,0),rect)
    else:
        rect = pygame.Rect(sheet.get_rect())
        image = pygame.Surface(rect.size)
        image.blit(sheet,(0,0),rect)
    return image


def prepare_sprite(sprite,color,size):
    """Take in a sprite and make its background transparent and change its size"""
    sprite.set_colorkey(color)
    return pygame.transform.scale(sprite,size)

def prepare_sprites(sprites,color,size):
    """Take in a list of sprites and make their background transparent and change their size"""
    t_sprites = []
    for sprite in sprites:
        t_sprites.append(pygame.transform.scale(sprite,size))  
    for sprite in t_sprites:
        sprite.set_colorkey(color) 
    return t_sprites

def flip(sprites):
    """Flip a list of sprites"""
    f_sprites = []
    for sprite in sprites:
        if type(sprite) is list:
            f_sprites.append([])
            for s in sprite:
                f_sprites[-1].append(pygame.transform.flip(s,True,False))
        else:
            f_sprites.append(pygame.transform.flip(sprite,True,False))
    return f_sprites
mega_walkRight = []
mega_shootRight = []
run = True
i = 0
for x in range(0,10):
    mega_walkRight.append(get_sprite("megaman/mega_walkRight" + str(x) + ".png"))
    mega_shootRight.append(get_sprite("megaman/mega_shootright" + str(x) + ".png"))
#i = 0
#while run:
    #pygame.time.delay(1000)
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
        #run = False
    #window.blit(mega_walkRight[i],(100,100))
    #pygame.display.update()
    #i += 1

bg = pygame.image.load(bg)
bg = prepare_sprite(bg,(0,0,0),(1000,1000))
platform = get_sprite(platform)
platform = prepare_sprite(platform,(255,255,255), (1000,25))
mega_walkright = prepare_sprites(mega_walkRight,(255,255,255),(64,64))
mega_idle = get_sprite("megaman/mega_idle.png")
mega_idle_right = prepare_sprite(mega_idle,(255,255,255),(64,64))
mega_shootright = prepare_sprites(mega_shootRight,(255,255,255),(64,64))
mega_shootidle = get_sprite("megaman/mega_shootidle.png")
mega_shootidle = prepare_sprite(mega_shootidle,(255,255,255),(78,64))
mega_jump = get_sprite("megaman/mega_jump.png")
mega_jump = prepare_sprite(mega_jump,(255,255,255), (80,64))
mega_jumpshoot = get_sprite("megaman/mega_shootjump.png")
mega_jumpshoot = prepare_sprite(mega_jumpshoot, (255,255,255), (80,64))
mega_sprites_right = [mega_walkright,mega_idle_right,mega_shootright,mega_shootidle,mega_jump,mega_jumpshoot]
mega_sprites_left = flip(mega_sprites_right)
print(mega_sprites_left)