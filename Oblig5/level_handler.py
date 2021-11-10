import pygame
import json
import time

from cust_const import *
from spritesheet import SpriteSheet
from player import Player

class LevelHandler():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(SpriteSheet().get_sprite( SPRITE_KEYS[PLAYER] ), screen)
        self.wall_sprite = SpriteSheet().get_sprite(SPRITE_KEYS[WALL])
        self.box_sprite = SpriteSheet().get_sprite(SPRITE_KEYS[BOX])
        self.goal_sprite = SpriteSheet().get_sprite(SPRITE_KEYS[GOAL])
        self._clear_level()

    def _clear_level(self):
        '''Clear the level by setting variables back to default'''
        self.name = "None"
        self.author = "Not Set"
        self.level_int = 0
        self.level_count = 0
        self.player_start_pos = (0, 0)
        self.map_data = []
        self.walls = []
        self.boxes = {}
        self.goals = []
    
    def reset_level(self):
        current_level = self.level_int
        self._clear_level()
        self.set_level(current_level)
    
    def set_next_level(self):
        current_level = self.level_int
        
        # Will wrap around to the first level
        # TODO At the last level remove the option to continue
        if current_level + 1 > self.level_count:
            self._clear_level()
            self.set_level(1)
        else:
            self._clear_level()
            self.set_level(current_level + 1)

    def set_level(self, level: int):
        '''Sets the level and loads everything. Levels starts at 1'''
        # TODO Improvement: Instead of creating a new sprite for every object in the level, rather 
        # just make a rect for every object and then they inherit the same image
        if level <= 0:
            self._clear_level()
            return
        
        with open("resources/level_data.json") as file:
            json_obj = json.load(file)

            if level > len(json_obj):
                self._clear_level()
                return
            
            self.map_data = json_obj[level - 1]['level_data']
            self.name =     json_obj[level - 1]['name']
            self.author =   json_obj[level - 1]['author']
            self.level_int = level
            self.level_count = len(json_obj)
        
        for y in range( len(self.map_data) ):
            for x in range( len(self.map_data[y]) ):
                current_char = self.map_data[y][x]
                
                if current_char == BLANK:  # Skip empty space
                    continue
                elif current_char == PLAYER:    # Saves the players start position in the level
                    self.player_start_pos = (x * SPRITE_SIZE, y * SPRITE_SIZE)
                    self.player.sprite.rect.topleft = self.player_start_pos
                    continue

                sprite_rect = pygame.Rect(x * SPRITE_SIZE, y * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE) # Position for screen

                if current_char == WALL:
                    self.walls.append(sprite_rect)
                elif current_char == BOX:
                    key_str = f"box_{len(self.boxes)}"
                    self.boxes[key_str] = sprite_rect
                elif current_char == GOAL:
                    self.goals.append(sprite_rect)
    
    def check_win_status(self) -> bool:
        '''Checking if all the boxes are in a goal
        
        return True if won, False if not'''
        all_boxes_over_goal = True
        for goal in self.goals:
            has_box_inside = False

            for box in self.boxes.values():
                if goal.colliderect(box):
                    has_box_inside = True
                    break
            
            if not has_box_inside:
                all_boxes_over_goal = False
        
        return all_boxes_over_goal

    def draw(self):
        # Check if there is a level to draw
        if len(self.map_data) == 0:
            return
        
        for wall in self.walls:
            self.screen.blit(self.wall_sprite.image, wall)
        for goal in self.goals:
            self.screen.blit(self.goal_sprite.image, goal)
        for box in self.boxes.values():
            self.screen.blit(self.box_sprite.image, box)
        
        self.player.draw()