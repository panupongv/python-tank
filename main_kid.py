import pygame, sys, time

from bots.bot_sample_a import BotSampleA
from bots.bot_sample_b import BotSampleB
from bots.bot_a import BotA
from bots.bot_b import BotB

from core.constants import *
from core.tank import TankInfo
from core.namedisplay import TimeDisplay

class Game:
    def __init__(self):
        self.prepare_game()
        
        tank_tawan = BotSampleA(self, 'sample A', 'green', 1, 1, 'right', self.sprite_list, self.tank_list)
        tank_eit   = BotSampleB(self, 'sample B', "green", 8, 8, "left", self.sprite_list, self.tank_list)
        tank_most  = BotA(self, 'A', "red", 8, 1, "up", self.sprite_list, self.tank_list)
        tank_guy   = BotB(self, 'B', "red", 1, 8, "down", self.sprite_list, self.tank_list)

    
        self.__tank_info_list = [ TankInfo(tank) for tank in self.tank_list ]

    def prepare_game(self):
        pygame.init()
        pygame.display.set_caption("Tank game")
        pygame.mixer.init()

        self.background = pygame.image.load("source/bg.png")
        self.red_won = pygame.image.load("source/red_won.png")
        self.green_won = pygame.image.load("source/green_won.png")
        self.draw = pygame.image.load("source/draw.png")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        
        self.sprite_list = pygame.sprite.Group()
        self.tank_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()

        self.timeleft = MATCH_TIME
        self.__timeleftdisplay = TimeDisplay("...",TIME_LABLE_SIZE)
        
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
            if winner == "":
                self.__drawTimeLeft()
            self.sprite_list.draw(self.screen)
            for tank in self.tank_list:
                tank.drawBars(self.screen)
            if winner == "draw":
                self.screen.blit(self.draw, [0, (SCREEN_WIDTH - BLOCK_SIZE)/2])
            elif winner == "green":
                self.screen.blit(self.green_won, [0, (SCREEN_WIDTH - BLOCK_SIZE)/2])
            elif winner == "red":
                self.screen.blit(self.red_won, [0, (SCREEN_WIDTH - BLOCK_SIZE)/2])
            pygame.display.update()

            ##Logics
            if self.lost("red") and self.lost("green"):
                winner = "draw"
            elif self.lost("green"):
                winner = "red"
            elif self.lost("red"):
                winner = "green"
            [ func() for func in self.__hidden_update_list ]
            self.clearDestroyedTankInfo()
            if winner != "draw":
                for s in self.sprite_list:
                    s.update()
            #self.sprite_list.update()
            self.processEvents()
            self.clock.tick(FPS)
            if winner == "":
                self.timeleft -= (1 / FPS)
                if self.timeleft < 0:
                    winner = "draw"



Game().main()
