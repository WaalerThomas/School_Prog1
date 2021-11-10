import pygame

from cust_const import *
from scene_handler import SceneHandler
from scene import *

class Game():
    def __init__(self, title):
        self.FPS_CAP = 60
        self.TITLE = title
        
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.is_running = True
        self.size = (800, 600)
        self.display_surf = pygame.Surface
        
        self.scene_handler = SceneHandler

    def update(self):
        '''Update surface from surface buffer'''
        pygame.display.update()
        self.delta_time = self.clock.tick(self.FPS_CAP)
        pygame.display.set_caption(f"{self.TITLE} - {round(self.clock.get_fps(), 1)}FPS {self.delta_time}ms")

    def run(self):
        '''Initialize pygame and run main game loop'''
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.TITLE)
        
        self.scene_handler = SceneHandler()
        mainmenu_scene = Scene_MainMenu(self.display_surf, self.scene_handler, self)
        game_scene = Scene_Game(self.display_surf, self.scene_handler, self)
        self.scene_handler.add_scene("MainMenu", mainmenu_scene)
        self.scene_handler.add_scene("Game", game_scene)
        self.scene_handler.set_scene("MainMenu")    # Sets the current scene

        # Main game loop
        while self.is_running:
            self.scene_handler.check_events()
            self.scene_handler.draw()
            self.update()
        
        # Cleanup
        # -------
        pygame.display.quit()
        pygame.quit()
        # -------


# Main game entry
if __name__ == "__main__":
    sokoban = Game("Sokoban")
    sokoban.run()
