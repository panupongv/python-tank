import pygame

from core.constants import *

class NameDisplay:
    def __init__(self, name):
        self.name = name
        self.font = pygame.font.Font("source/waan.ttf", 50)
        self.text = self.font.render(name, True, WHITE)
        
    def draw(self, screen, x, y):
        x += BLOCK_SIZE / 2
        x -= self.text.get_width() / 2
        y += BLOCK_SIZE - self.text.get_height()
        screen.blit(self.text, [x, y])        
