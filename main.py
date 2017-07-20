import pygame, sys, time

from bots.bot_tawan import BotTawan
from bots.bot_guy import BotGuy
from bots.bot_most import FuckBot420
from bots.bot_eit import BotEit

from core.constants import *
from core.tank import TankInfo
from core.namedisplay import NameDisplay

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tank game")
        pygame.mixer.init()

        self.background = pygame.image.load("source/bg.png")
        self.red_won = pygame.image.load("source/red_won.png")
        self.green_won = pygame.image.load("source/green_won.png")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([650, 650])
        
        self.sprite_list = pygame.sprite.Group()
        self.tank_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()

        self.timeleft = MATCH_TIME
        self.__timeleftdisplay = NameDisplay("...",300)

        tank_tawan = BotTawan(self, 'tawan', 'green', 0, 0, 'right', self.sprite_list, self.tank_list)
        tank_most = FuckBot420(self, 'fuck bot 420', "red", 9, 0, "up", self.sprite_list, self.tank_list)
        tank_guy = BotGuy(self, 'guy', "red", 0, 9, "down", self.sprite_list, self.tank_list)
        tank_eit = BotEit(self, 'eit', "green", 9, 9, "left", self.sprite_list, self.tank_list)
    
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
        for i,t in enumerate(self.__tank_info_list) :
            if t.isDead() :
                del self.__tank_info_list[i]
                break
        
    def getTankInfoList(self):
        return self.__tank_info_list[:]

    def lost(self, team_color):
        for tank in self.tank_list:
            if tank.getTeamColor() == team_color:
                return False
        return True

    def __drawTimeLeft(self):
        timetext = str(int(self.timeleft // 60)) + ":" + format(int(self.timeleft % 60),"02d")
        self.__timeleftdisplay.updateText(timetext)
        self.__timeleftdisplay.draw(self.screen,SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2)


    def main(self):
        winner = ""
        while True:
            ##Drawings
            self.screen.blit(self.background, [0, 0])
            self.__drawTimeLeft()
            self.sprite_list.draw(self.screen)
            for tank in self.tank_list:
                tank.drawBars(self.screen)
            if winner == "green":
                self.screen.blit(self.green_won, [0, (SCREEN_WIDTH - BLOCK_SIZE)/2])
            elif winner == "red":
                self.screen.blit(self.red_won, [0, (SCREEN_WIDTH - BLOCK_SIZE)/2])
            pygame.display.update()

            ##Logics
            if self.lost("red"):
                winner = "green"
            elif self.lost("green"):
                winner = "red"
            [ func() for func in self.__hidden_update_list ]
            self.clearDestroyedTankInfo()
            self.sprite_list.update()
            self.processEvents()
            self.clock.tick(FPS)
            self.timeleft -= (1 / FPS)



Game().main()
