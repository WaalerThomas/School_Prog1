import pygame
import pygame_gui
import time

from cust_const import *
from level_handler import LevelHandler

class Scene:
    def __init__(self, screen: pygame.Surface, handler, parent):
        self.screen = screen
        self.parent = parent
        self.handler = handler

    def init(self):
        pass

    def check_events(self):
        pass

    def draw(self):
        pass

class Scene_MainMenu(Scene):
    def __init__(self, screen: pygame.Surface, handler, parent):
        Scene.__init__(self, screen, handler, parent)
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent.is_running = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    self.handler.set_scene("Game")

    def draw(self):
        self.screen.fill(WHITE)

class Scene_Loading(Scene):
    def __init__(self, screen: pygame.Surface, handler, parent):
        Scene.__init__(self, screen, handler, parent)
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent.is_running = False

    def draw(self):
        pass

class Scene_Game(Scene):
    def __init__(self, screen: pygame.Surface, handler, parent):
        Scene.__init__(self, screen, handler, parent)
        self.show_ui_debug = False

        self.header_font = pygame.font.Font
        self.gui_manager = pygame_gui.UIManager
        self.btn_reset_level = pygame_gui.elements.UIButton
        self.btn_back = pygame_gui.elements.UIButton

        self.level_handler = LevelHandler
    
    def init(self):
        # Setup GUI
        # ---------
        self.gui_manager = pygame_gui.UIManager(self.parent.size)
        
        btn_back_rect = pygame.Rect(0, 0, 70, 40)
        btn_back_rect.bottomleft = (5, -5)
        self.btn_back = pygame_gui.elements.UIButton(btn_back_rect, "< Back", self.gui_manager, anchors={"left": "left", "right": "left", "top": "bottom", "bottom": "bottom"})
        
        btn_reset_level_rect = pygame.Rect(0, 0, 150, 40)
        btn_reset_level_rect.bottomleft = (btn_back_rect.right + 5, -5)
        self.btn_reset_level = pygame_gui.elements.UIButton(btn_reset_level_rect, text="Reset level (R)", manager=self.gui_manager, anchors={"left": "left", "right": "left", "top": "bottom", "bottom": "bottom"})
        
        self.header_font = pygame.font.SysFont(pygame.font.get_default_font(), 48)
        # ---------

        start_time = time.time()
        self.level_handler = LevelHandler(self.screen)
        self.level_handler.set_level(2)
        print(f"Wall count: {len(self.level_handler.walls)}")
        print(f"Box count: {len(self.level_handler.boxes)}")
        print(f"Goal count: {len(self.level_handler.goals)}")
        end_time = time.time()
        print(f"Took {int((end_time - start_time) * 1000)}ms to create level")

    def move(self, direction: tuple, check_collision: bool=True):
        '''Move the player in a direction'''
        rect = self.level_handler.player.get_rect()
        rect.topleft = (rect.x + (direction[0] * SPRITE_SIZE), rect.y + (direction[1] * SPRITE_SIZE))

        # Check for collisions
        if check_collision:
            for wall in self.level_handler.walls:
                if rect.colliderect(wall):
                    new_direction = (-direction[0], -direction[1])
                    self.move(new_direction, False)
                    break
            
            for key, value in self.level_handler.boxes.items():
                if rect.colliderect(value) and not self.push_box(key, direction):
                    new_direction = (-direction[0], -direction[1])
                    self.move(new_direction, False)
                    break

    def push_box(self, box_key: str, direction: tuple) -> bool:
        '''Push a given box sprite in a direction
        box: The sprite of the box to be moved
        direction: A tuple saying which direction to be pushed
        
        return True or False if it could be pushed or not'''
        rect = self.level_handler.boxes.get(box_key)
        rect.topleft = (rect.x + (direction[0] * SPRITE_SIZE), rect.y + (direction[1] * SPRITE_SIZE))

        # Check for collisions
        for wall in self.level_handler.walls:
            if rect.colliderect(wall):
                new_direction = (-direction[0], -direction[1])
                rect.topleft = (rect.x + (new_direction[0] * SPRITE_SIZE), rect.y + (new_direction[1] * SPRITE_SIZE))
                return False
        
        for key, value in self.level_handler.boxes.items():
            if rect.colliderect(value) and not box_key == key:
                new_direction = (-direction[0], -direction[1])
                rect.topleft = (rect.x + (new_direction[0] * SPRITE_SIZE), rect.y + (new_direction[1] * SPRITE_SIZE))
                return False
        
        for goal in self.level_handler.goals:
            if rect.colliderect(goal):
                if self.level_handler.check_win_status():
                    self.win_level()
        
        return True
    
    def win_level(self):
        print("You Won!!!")

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent.is_running = False

            if event.type == pygame.KEYDOWN:
                # Player movement
                if event.key == pygame.K_UP:
                    self.move( (0, -1) )
                if event.key == pygame.K_DOWN:
                    self.move( (0, 1) )
                if event.key == pygame.K_LEFT:
                    self.move( (-1, 0) )
                if event.key == pygame.K_RIGHT:
                    self.move( (1, 0) )
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:    # Exit the game with escape
                    self.parent.is_running = False
                
                if event.key == pygame.K_p: # Show debug layer of the gui
                    self.gui_manager.set_visual_debug_mode(not self.show_ui_debug)
                    self.show_ui_debug = not self.show_ui_debug

                if event.key == pygame.K_r: # Reset level
                    self.level_handler.reset_level()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.btn_reset_level:
                        self.level_handler.reset_level()
                    
                    if event.ui_element == self.btn_back:
                        self.parent.scene_handler.set_previous_scene()

            self.gui_manager.process_events(event)

        Scene.check_events(self)

    def draw(self):
        self.gui_manager.update(self.parent.delta_time)

        self.screen.fill(TEAL)
        self.level_handler.draw()

        header_surface = self.header_font.render(self.level_handler.name, False, (207, 198, 184))
        self.screen.blit(header_surface, (self.parent.size[0] / 2, self.parent.size[1] - 50))

        self.gui_manager.draw_ui(self.screen)