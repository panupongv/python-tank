import pygame

from core.constants import *

class NameDisplay:
    def __init__(self, content, size = 50):
        self.font = pygame.font.Font("source/waan.ttf", size)
        self.text = self.font.render(content, True, WHITE)
        
    def draw(self, screen, x, y):
        x += BLOCK_SIZE / 2
        x -= self.text.get_width() / 2
        y += BLOCK_SIZE - self.text.get_height()
        screen.blit(self.text, [x, y])

    def updateText(self, new_content):
        self.text = self.font.render(new_content, True, WHITE)

class TimeDisplay(NameDisplay):
    def draw(self, screen, x, y):
        x -= self.text.get_width() / 2
        y -= self.text.get_height() / 2
        screen.blit(self.text, [x, y])