import pygame
from cust_const import SPRITE_SIZE

class SpriteSheet:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls._instance = super(SpriteSheet, cls).__new__(cls)
            cls._sheet = pygame.image.load("resources/colored_transparent_packed.png").convert_alpha()
        
        return cls._instance
    
    @staticmethod
    def get_sprite(index: tuple) -> pygame.sprite.Sprite:
        '''Get a sprite from a spritesheet. index: position of sprite'''
        sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect( (index[0] * SPRITE_SIZE, index[1] * SPRITE_SIZE), (SPRITE_SIZE, SPRITE_SIZE) ) # Where in the spritesheet to get the image
        sprite.image = pygame.Surface(sprite.rect.size, pygame.SRCALPHA)
        sprite.image.blit(SpriteSheet()._sheet, (0, 0), sprite.rect)

        # Reset the rect position
        sprite.rect.topleft = (0, 0) # Position for screen
        return sprite