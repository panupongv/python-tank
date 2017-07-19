import pygame

from constants import *
from bullet import Bullet_Heal, Bullet_Damage

class Tank(pygame.sprite.Sprite):
    def __init__(self, game, name, team_color, x, y, direction, *group):
        super(Tank, self).__init__(*group)
        self.__team_color = team_color
        self.__name = name
        self.images = [pygame.image.load(team_color + "_tank_left.png"),
                       pygame.image.load(team_color + "_tank_right.png"),
                       pygame.image.load(team_color + "_tank_up.png"),
                       pygame.image.load(team_color + "_tank_down.png"),]
        self.__direction = direction
        self.image = self.images[self.__getIndex()]
        self.rect = self.image.get_rect()
        
        self.__grid_x = x
        self.__grid_y = y

        self.__shoot_cooldown = SHOOT_COOLDOWN
        self.__move_cooldown = MOVE_COOLDOWN

        self.__game = game

    def isAlly(self, tank):
        return self.__team_color == tank.getTeamColor()

    def getTeamColor(self):
        return self.__team_color

    def readyToMove(self):
        return self.__move_cooldown <= 0

    def readyToShoot(self):
        return self.__shoot_cooldown <= 0

    def __update_cooldown(self, game) :
        self.__move_cooldown -= game.getDeltaTime()
        self.__shoot_cooldown -= game.getDeltaTime()
            
    def update(self, game):
        self.shoot("down", game)
        self.__update_cooldown(game)
        self.__right()
        self.rect.x = self.__grid_x * BLOCK_SIZE
        self.rect.y = self.__grid_y * BLOCK_SIZE

    def __resetMoveCooldown(self):
        self.__move_cooldown = MOVE_COOLDOWN

    def __resetShootCooldown(self):
        self.__shoot_cooldown = SHOOT_COOLDOWN
        
    def __left(self):
        if not self.readyToMove() :
            return
        
        if self.__grid_x > 0:
            self.__grid_x -= 1
        self.image = self.images[0]

        self.__resetMoveCooldown()
        
    def __right(self):
        if not self.readyToMove() :
            return 
        if self.__grid_x < 9:
            self.__grid_x += 1
        self.image = self.images[1]
        
        self.__resetMoveCooldown()
        
    def __up(self):
        if not self.readyToMove() :
            return 
        if self.__grid_y > 0:
            self.__grid_x -= 1
        self.image = self.images[2]
        
        self.__resetMoveCooldown()
        
    def __down(self):
        if not self.readyToMove() :
            return 
        if self.__grid_y < 9:
            self.__grid_x += 1
        self.image = self.images[3]
        
        self.__resetMoveCooldown()

    def shoot(self, direction, game):
        if self.readyToShoot():
            bullet = Bullet_Damage(self, direction, game.sprite_list, game.bullet_list)
            self.__resetShootCooldown()

    def heal(self, direction, game):
        if self.readyToShoot():
            bullet = Bullet_Health(self, direction, game.sprite_list, game.bullet_list)
            self.__resetShootCooldown() 
            
    def getName(self):
        return self.__name

    def getPosition(self):
        return self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE

    def __getIndex(self):
        if self.__direction == "left": return 0
        if self.__direction == "right": return 1
        if self.__direction == "up": return 2
        if self.__direction == "down": return 3

  
