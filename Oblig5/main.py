import pygame
from pygame.locals import *
import json

# Colours
TEAL = (0, 121, 107)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def get_level_map(index: int) -> list:
    '''Returns the map data of given index.
    Starts at 1
    
    Return 'List' of map. 'None' if failed'''
    if index <= 0:
        return None

    with open("level_data.json") as file:
        json_obj = json.load(file)
        
        # Check if level index exist
        if index > len(json_obj):
            return None
        
        print(len(json_obj))


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

        some_sprite = pygame.sprite.Sprite()
        some_sprite.image = pygame.image.load("resources/player.png")
        some_sprite.rect = some_sprite.image.get_rect()
        some_sprite.rect.topleft = (200, 200)

        while self.is_running:
            # Go through all events that has arisen 
            for event in pygame.event.get():
                self.on_event(event)
            
            self.display_surf.fill(TEAL)
            self.display_surf.blit(some_sprite.image, some_sprite.rect)
            
            # Render everything
            pygame.display.update()
            self.delta_time.tick(self.FPS_CAP)
        
        # Cleanup
        pygame.display.quit()
        pygame.quit()


# Main game entry
if __name__ == "__main__":
    get_level_map(0)
    #sokoban = Game("Sokoban")
    #sokoban.run()