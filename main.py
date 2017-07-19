import pygame, sys, time

from bots.bot_sample import BotSample
from core.constants import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tank game")
        pygame.mixer.init()

        self.background = pygame.image.load("source/bg.png")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([650, 650])
        
        self.sprite_list = pygame.sprite.Group()
        self.tank_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        
        tank1 = BotSample(self, 1, "green", 0, 0, "right", self.sprite_list, self.tank_list)

    def processEvents(self):
            self.mouseX, self.mouseY = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
    def main(self):
        while True:
            self.screen.blit(self.background, [0, 0])
            self.sprite_list.update()
            self.sprite_list.draw(self.screen)
            pygame.display.update()
            
            self.processEvents()
            self.clock.tick(FPS)

Game().main()
