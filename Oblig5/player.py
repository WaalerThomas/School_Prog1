import pygame

class Player:
    def __init__(self, sprite, screen):
        self.sprite = sprite
        self.screen = screen

    def update(self, delta_time):
        pass

    def draw(self):
        self.screen.blit(self.sprite.image, self.sprite.rect)
    
    def get_rect(self) -> pygame.Rect:
        return self.sprite.rect