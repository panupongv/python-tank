import pygame
import time
import sys

from core.tank import *

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
        
        tank1 = Tank(self, 1, "green", 0, 0, "right", self.sprite_list, self.tank_list)

        self.__time_last_frame = -1

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

            self.__time_last_frame = time.time()
            self.clock.tick(FPS)

Game().main()
