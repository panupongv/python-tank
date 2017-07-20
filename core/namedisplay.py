import pygame

from constants import *

class NameDisplay:
    def __init__(self, name, x, y):
        self.name = name
        self.font = pygame.font.Font("source/waan.ttf")
        self.text = self.font.render(name, True, WHITE)
        
    def draw(self, screen, x, y):
        screen.blit(self.text, [x, y])        
