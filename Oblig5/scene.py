import pygame
import pygame_gui

from cust_const import *
from level_handler import LevelHandler

class Scene:
    '''Base class for all scenes'''
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
        self.show_ui_debug = False

        self.gui_manager = pygame_gui.UIManager
        self.btn_level_select = pygame_gui.elements.UIButton
        self.btn_exit = pygame_gui.elements.UIButton

        self.header_font = pygame.font.Font
    
    def init(self):
        # Setup GUI
        # ---------
        self.gui_manager = pygame_gui.UIManager(self.parent.size)
        self.header_font = pygame.font.SysFont("Arial", 48, True)

        btn_level_select_rect = pygame.Rect(30, 20, 120, 40)
        btn_level_select_rect.center = (self.parent.size[0] / 2, self.parent.size[1] / 2)
        self.btn_level_select = pygame_gui.elements.UIButton(btn_level_select_rect, "Play", self.gui_manager)
        
        btn_exit_rect = pygame.Rect(0, 0, 120, 40)
        btn_exit_rect.topleft = (btn_level_select_rect.x, btn_level_select_rect.bottom + 10)
        self.btn_exit = pygame_gui.elements.UIButton(btn_exit_rect, "Exit", self.gui_manager)
        # ---------

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent.is_running = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p: # Show debug layer of the gui
                    self.gui_manager.set_visual_debug_mode(not self.show_ui_debug)
                    self.show_ui_debug = not self.show_ui_debug

                if event.key == pygame.K_t:
                    self.handler.set_scene("Game")
            
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.btn_exit:
                        self.parent.is_running = False
                    
                    if event.ui_element == self.btn_level_select:
                        self.handler.set_scene("Game")
            
            self.gui_manager.process_events(event)

    def draw(self):
        self.gui_manager.update(self.parent.delta_time)
        self.screen.fill(DARK_BLUE)

        header_surface = self.header_font.render("Sokoban", False, WHITE_2)
        self.screen.blit(header_surface, ((self.parent.size[0] / 2) - (header_surface.get_size()[0] / 2), 30))

        self.gui_manager.draw_ui(self.screen)


class Scene_Game(Scene):
    def __init__(self, screen: pygame.Surface, handler, parent):
        Scene.__init__(self, screen, handler, parent)
        self.show_ui_debug = False
        self.has_won = False

        self.header_font = pygame.font.Font
        self.gui_manager = pygame_gui.UIManager
        self.pnl_win = pygame_gui.elements.UIPanel
        self.btn_continue = pygame_gui.elements.UIButton
        self.btn_win_back = pygame_gui.elements.UIButton
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
        
        pnl_win_rect = pygame.Rect(0, 0, 300, 90)
        pnl_win_rect.center = (self.parent.size[0] / 2, self.parent.size[1] / 2)
        self.pnl_win = pygame_gui.elements.UIPanel(pnl_win_rect, 1, self.gui_manager)
        self.pnl_win.hide()

        lbl_win_rect = pygame.Rect(0, 0, 100, 40)
        lbl_win_rect.topleft = (100, 0)
        lbl_win = pygame_gui.elements.UILabel(lbl_win_rect, "YOU WON!!", self.gui_manager, self.pnl_win, anchors={"left": "left", "right": "right", "top": "top", "bottom": "top"})

        btn_continue_rect = pygame.Rect(0, 0, 120, 40)
        btn_continue_rect.bottomright = (-5, -5)
        self.btn_continue = pygame_gui.elements.UIButton(btn_continue_rect, "Next Level >", self.gui_manager, self.pnl_win, anchors={"left": "right", "right": "right", "top": "bottom", "bottom": "bottom"})

        btn_win_back_rect = pygame.Rect(0, 0, 120, 40)
        btn_win_back_rect.bottomleft = (5, -5)
        self.btn_win_back = pygame_gui.elements.UIButton(btn_win_back_rect, "< Main Menu", self.gui_manager, self.pnl_win, anchors={"left": "left", "right": "left", "top": "bottom", "bottom": "bottom"})

        self.header_font = pygame.font.SysFont(pygame.font.get_default_font(), 48)
        # ---------

        self.level_handler = LevelHandler(self.screen)
        self.level_handler.set_level(1)

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
        self.has_won = True
        self.pnl_win.show()
        self.btn_back.hide()
        self.btn_reset_level.hide()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent.is_running = False

            if event.type == pygame.KEYDOWN:
                # Player movement
                if not self.has_won:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.move( (0, -1) )
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.move( (0, 1) )
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.move( (-1, 0) )
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.move( (1, 0) )
            
            if event.type == pygame.KEYUP:                
                if event.key == pygame.K_p: # Show debug layer of the gui
                    self.gui_manager.set_visual_debug_mode(not self.show_ui_debug)
                    self.show_ui_debug = not self.show_ui_debug

                if event.key == pygame.K_r: # Reset level
                    self.level_handler.reset_level()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.btn_reset_level:
                        self.level_handler.reset_level()
                    
                    if event.ui_element == self.btn_back or event.ui_element == self.btn_win_back:
                        self.parent.scene_handler.set_previous_scene()
                        self.has_won = False
                    
                    if event.ui_element == self.btn_continue:
                        self.level_handler.set_next_level()
                        self.has_won = False
                        self.pnl_win.hide()
                        self.btn_back.show()
                        self.btn_reset_level.show()

            self.gui_manager.process_events(event)

    def draw(self):
        self.gui_manager.update(self.parent.delta_time)

        self.screen.fill(TEAL)
        self.level_handler.draw()

        header_surface = self.header_font.render(self.level_handler.name, False, (207, 198, 184))
        self.screen.blit(header_surface, ((self.parent.size[0] / 2) - (header_surface.get_size()[0] / 2), self.parent.size[1] - header_surface.get_size()[1] - 5))

        self.gui_manager.draw_ui(self.screen)