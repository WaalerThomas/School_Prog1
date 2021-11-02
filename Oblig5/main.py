import pygame
from pygame.draw import rect
from pygame.locals import *

import json
from dataclasses import dataclass

# http://borgar.net/programs/sokoban/#Sokoban

# Colours
# -------
TEAL = (0, 121, 107)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# -------

SPRITE_SIZE = 32

# Dictionary of sprite positions in the spritesheet
sprite_keys = {
    " ": (0, 0),    # Floor
    "#": (0, 13),   # Solid Wall
    "@": (24, 0),   # Player
    "B": (15, 14),  # Box
    "G": (35, 12),  # Goal
}

def get_level_map(index: int) -> list:
    '''Returns the map data of given index.
    Starts at 1
    
    Return 'List' of map. 'None' if failed'''
    if index <= 0:
        return None

    with open("level_data.json") as file:
        json_obj = json.load(file)
        
        if index > len(json_obj):
            return None

        return json_obj[index - 1]['level_data']

def get_sprite_map(level_data: list) -> list:
    sprite_list = []
    sprite_sheet = pygame.image.load("resources/colored_transparent_packed.png").convert_alpha()

    for y in range( len(level_data) ):
        for x in range( len(level_data[y]) ):
            sprite_pos = sprite_keys[ level_data[y][x] ]

            sprite = pygame.sprite.Sprite()
            sprite.rect = pygame.Rect((sprite_pos[0] * SPRITE_SIZE, sprite_pos[1] * SPRITE_SIZE), (32, 32))   # Where in the spritesheet to get the image
            sprite.image = pygame.Surface(sprite.rect.size, pygame.SRCALPHA)
            sprite.image.blit(sprite_sheet, (0, 0), sprite.rect)

            sprite.rect.topleft = (x * 32, y * 32)    # Position for screen
            sprite_list.append(sprite)
    
    return sprite_list

class Level():
    pass


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()


class Game():
    def __init__(self, title) -> None:
        self.FPS_CAP = 60
        self.TITLE = title
        
        self.delta_time = pygame.time.Clock()
        self.is_running = True
        self.size = (800, 600)
        self.display_surf = None

    def on_event(self, event):
        '''Handle given event'''
        if event.type == QUIT:
            self.is_running = False

    def run(self):
        '''Initialize pygame and run main game loop'''
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.TITLE)

        

        #my_level = get_sprite_map( get_level_map(2) )

        while self.is_running:
            # Go through all events that has arisen 
            for event in pygame.event.get():
                self.on_event(event)
            
            self.display_surf.fill(TEAL)
            #for sprt in my_level:
            #    self.display_surf.blit(sprt.image, sprt.rect)
            
            # Render everything
            pygame.display.update()
            self.delta_time.tick(self.FPS_CAP)
        
        # Cleanup
        pygame.display.quit()
        pygame.quit()


# Main game entry
if __name__ == "__main__":
    sokoban = Game("Sokoban")
    sokoban.run()