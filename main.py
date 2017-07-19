import pygame
import time
import sys

from Tank import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tank game")
        pygame.mixer.init()

        self.background = pygame.image.load("bg.png")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([650, 650])
        self.tank_list = pygame.sprite.Group()
        tank1 = Tank("red", 1, "red", 0, 0, "right", self.tank_list)

        self.__time_last_frame = -1

    def processEvents(self):
            self.mouseX, self.mouseY = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def getDeltaTime(self) :
        return time() - self.__time_last_frame
                
    def main(self):
        while True:
            self.screen.blit(self.background, [0, 0])
            #self.tank_list.update(self)
            for i in self.tank_list:
                i.update(self)
                print(i.getPosition())
            self.tank_list.draw(self.screen)
            pygame.display.update()
            self.processEvents()
            self.clock.tick(1)

            self.__time_last_frame = time()

Game().main()
