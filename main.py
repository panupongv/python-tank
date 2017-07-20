import pygame, sys, time

from bots.bot_tawan import BotTawan
from bots.bot_guy import BotGuy
from bots.bot_most import FuckBot420
from bots.bot_eit import BotEit

from core.constants import *
from core.tank import TankInfo

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
        
        tank_tawan = BotTawan(self, 0, 'green', 0, 0, 'right', self.sprite_list, self.tank_list)
        tank_most = FuckBot420(self, 1, "red", 9, 0, "up", self.sprite_list, self.tank_list)
        tank_guy = BotGuy(self, 2, "red", 0, 9, "down", self.sprite_list, self.tank_list)
        tank_eit = BotEit(self, 3, "green", 9, 9, "left", self.sprite_list, self.tank_list)
    
        self.__tank_info_list = [ TankInfo(tank) for tank in self.tank_list ]

    def add_hidden_update(self, func):
        try :
            a = type(self.__hidden_update_list)
        except :
            self.__hidden_update_list = []

        self.__hidden_update_list.append(func)
        
    def processEvents(self):
            self.mouseX, self.mouseY = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
    def clearDestroyedTankInfo(self):
        for t in self.__tank_info_list[:] :
            try :
                t.getName()
            except :
                self.__tank_info_list.remove(t)
        
    def getTankInfoList(self):
        return self.__tank_info_list[:]
    
    def main(self):
        while True:
            self.screen.blit(self.background, [0, 0])
            self.clearDestroyedTankInfo()
            [ func() for func in self.__hidden_update_list ]
            self.sprite_list.update()
            self.sprite_list.draw(self.screen)
            for tank in self.tank_list:
                tank.drawBars(self.screen)
            pygame.display.update()
            
            self.processEvents()
            self.clock.tick(FPS)

Game().main()
