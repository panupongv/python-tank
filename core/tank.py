import pygame

from core.constants import *
from core.bullet import Bullet_Heal, Bullet_Damage
from core.bar import Bar
from core.namedisplay import NameDisplay
from time import time as current_time
from math import pi, sin

class TankPrototype (pygame.sprite.Sprite):
    #constructor
    def __init__(self, game, name, team_color, x, y, direction, *group):
        super().__init__(*group)

        self.__name_tag = NameDisplay(name)
        self.__hp = Bar(RED, MAX_HP, MAX_HP, x * BLOCK_SIZE, y * BLOCK_SIZE) 
        self.__mp = Bar(BLUE, MAX_MP, MAX_MP, x * BLOCK_SIZE, y * BLOCK_SIZE + BAR_HEIGHT)
        self.__dead = False
        
        self.__team_color = team_color
        self.__name = name
        self.images = [pygame.image.load('source/' + team_color + "_tank_left.png"),
                       pygame.image.load('source/' + team_color + "_tank_right.png"),
                       pygame.image.load('source/' + team_color + "_tank_up.png"),
                       pygame.image.load('source/' + team_color + "_tank_down.png"),]
        self.__direction = direction
        self.image = self.images[self.__getIndex()]
        self.rect = self.image.get_rect()

        self.__grid_x = x
        self.__grid_y = y

        self.rect.x = x * BLOCK_SIZE
        self.rect.y = y * BLOCK_SIZE
        
        self.__is_moving = False
        self.__speed_x = 0
        self.__speed_y = 0
        
        self.__shoot_cooldown = SHOOT_COOLDOWN
        self.__move_cooldown = MOVE_COOLDOWN
        self.__move_counter = 0

        game.add_hidden_update(self.__hidden_update)
        self.__game = game
        self.start()

    #private methods ( internal use only, other cant use it, it's danger to allow so )
    def __checkBulletCollision(self):
        for bullet in self.__game.bullet_list:
            if bullet.isMakingContact(self):
                self.__hp -= bullet.getDamage()
                bullet.kill()
                if self.__hp <= 0:
                    self.__dead = True
                    self.rect.x = self.rect.y = -100
                    self.kill()
                elif self.__hp > MAX_HP:
                    self.__hp = MAX_HP
                return

    def __resetMoveCooldown(self):
        self.__move_cooldown = MOVE_COOLDOWN

    def __resetShootCooldown(self):
        self.__shoot_cooldown = SHOOT_COOLDOWN

    def __clamp_grid_pos(self):
        if self.__grid_x < 0 :
            self.__grid_x = 0
            
        if self.__grid_x > 9 :
            self.__grid_x = 9
            
        if self.__grid_y < 0 :
            self.__grid_y = 0
            
        if self.__grid_y > 9 :
            self.__grid_y = 9

    def __getIndex(self):
        if self.__direction == "left" : return 0
        if self.__direction == "right" : return 1
        if self.__direction == "up" : return 2
        if self.__direction == "down" : return 3
    
    def __clampOne(self, x) :
        if x > 1 :
            return 1
        
        return x
            
    def __updateMove(self) :
        if not self.isMoving() :
            return 
        from_x = self.__from_grid_x*BLOCK_SIZE
        from_y = self.__from_grid_y*BLOCK_SIZE
        to_x = self.__to_grid_x*BLOCK_SIZE
        to_y = self.__to_grid_y*BLOCK_SIZE
        time_since_start_move = current_time() - self.__start_move_time
        ratio = self.__clampOne(time_since_start_move/MOVE_TIME)
        angle = ratio*pi/2
        
        self.rect.x  = from_x + sin(angle)*(to_x - from_x)
        self.rect.y = from_y + sin(angle)*(to_y - from_y)
        
        if ratio >= 1 :
            self.__is_moving = False
            
    def __getTankInfoList(self):
        return self.__game.getTankInfoList()    
            
    def __hidden_update(self):
        self.__move_cooldown -= 1 / FPS
        self.__shoot_cooldown -= 1 / FPS
        self.__mp += MP_REGEN_RATE / FPS
        self.__updateMove()
                
        self.__hp.updatePosition(self.rect.x, self.rect.y)
        self.__mp.updatePosition(self.rect.x, self.rect.y + BAR_HEIGHT)

        self.__checkBulletCollision()

    #public methods
    def isDead(self):
        return self.__dead
        
    def getHP(self):
        return self.__hp.getValue()

    def getMP(self):
        return self.__mp.getValue()

    def getTeamColor(self):
        return self.__team_color
    
    def isAlly(self, tank):
        return self.__team_color == tank.getTeamColor()

    def readyToMove(self):
        return self.__move_cooldown <= 0 and not self.isMoving()

    def readyToShoot(self):
        return self.__shoot_cooldown <= 0 and self.getMP() >= DAMAGE_BULLET_MANA_COST
    
    def readyToHeal(self):
        return self.__shoot_cooldown <= 0 and self.getMP() >= HEAL_BULLET_MANA_COST    
        
    def move(self, direction) :
        if not self.readyToMove() :
            return
        
        if self.isAtEdge(direction) :
            return
        
        if self.isBlocked(direction) :
            return
        
        next_x = self.__grid_x
        next_y = self.__grid_y
        
        if direction == 'left' :
            next_x -= 1
        elif direction == 'right' :
            next_x += 1
        elif direction == 'up' :
            next_y -= 1
        elif direction == 'down' :
            next_y += 1
        else :
            raise ValueError('unknown direction given : ' + str(direction))
    
        self.__direction = direction
        self.image = self.images[self.__getIndex()]    
        self.__from_grid_x = self.__grid_x
        self.__from_grid_y = self.__grid_y
        self.__start_move_time = current_time()
    
        self.__is_moving = True
        
        self.__to_grid_x = next_x
        self.__to_grid_y = next_y
        self.__grid_x = next_x
        self.__grid_y = next_y

        # decrease mp when move
        self.__mp -= MOVE_MANA_COST 
        self.__resetMoveCooldown()

    def shoot(self, direction):
        if self.readyToShoot() and self.__mp.getValue() - DAMAGE_BULLET_MANA_COST >= 0:
            bullet = Bullet_Damage(self, direction, self.__game.sprite_list, self.__game.bullet_list)
            self.__resetShootCooldown()
            self.__mp -= DAMAGE_BULLET_MANA_COST

    def shoot_heal(self, direction):
        if self.readyToShoot() and self.__mp.getValue() - HEAL_BULLET_MANA_COST >= 0:
            bullet = Bullet_Heal(self, direction, self.__game.sprite_list, self.__game.bullet_list)
            self.__resetShootCooldown()
            self.__mp -= HEAL_BULLET_MANA_COST
            
    def getName(self):
        return self.__name

    def getPosition(self):
        return self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE

    def isMoving(self):
        return self.__is_moving
    
    def isAtEdge(self, direction):
        if direction == 'left' and self.__grid_x == 0 :
            return True
        if direction == 'right' and self.__grid_x == 9 :
            return True
        if direction == 'up' and self.__grid_y == 0 :
            return True
        if direction == 'down' and self.__grid_y == 9 :
            return True
        
        return False
    
    def isBlocked(self, direction) :
        mx, my = self.getPosition()
        
        if direction == 'left' :
            mx -= 1
        elif direction == 'right' :
            mx += 1
        elif direction == 'down' :
            my += 1
        elif direction == 'up' :
            my -= 1
        else :
            raise
        
        for t in self.getAllyList() :
            tx, ty = t.getPosition()
            if mx == tx and my == ty :
                return True
            
        return False
        
    def getDirection(self):
        return self.__direction
        
    def getAllyList( self ):
        ally_list = list()

        for tank in self.__getTankInfoList():
            if(self.getName() == tank.getName()):
                continue
            elif(self.isAlly(tank)):
                ally_list.append(tank)
        return ally_list
    
    def getEnemyList( self ):
        enemy_list = list()

        for tank in self.__getTankInfoList():
            if (self.getName() == tank.getName()):
                continue
            elif (not self.isAlly(tank)):
                enemy_list.append(tank)
        return enemy_list
    
    #for calling bars.draw() from main
    def drawBars(self, screen):
        self.__hp.draw(screen)
        self.__mp.draw(screen)
        self.__name_tag.draw(screen, self.rect.x, self.rect.y)
        
    #this is pseudo abstract method ( should be override )
    #the update process that should not be invoked from outside is in hidden_update() method
    def start(self):
        pass
    
    def update(self):
        pass
    
class TankInfo :
    def __init__(self, tank):
        self.__tank = tank
        
    def getHP(self):
        return self.__tank.getHP()
    
    def getMP(self):
        return self.__tank.getMP()
    
    def readyToMove(self):
        return self.__tank.readyToMove()
    
    def readyToShoot(self):
        return self.__tank.readyToShoot()
    
    def getName(self):
        return self.__tank.getName()
    
    def getPosition(self):
        return self.__tank.getPosition()
    
    def getTeamColor(self) :
        return self.__tank.getTeamColor()
    
    def isAlly(self, tank):
        return self.getTeamColor() == tank.getTeamColor()
    
    def isMySelf(self, my_tank) :
        return my_tank == self.__tank
    
    def isAtEdge(self, direction) :
        return self.__tank.isAtEdge(direction)
    
    def getDirection(self) :
        return self.__tank.getDirection()
    
    def isBlocked(self, direction) :
        return self.__tank.isBlocked(direction)
    
    def isDead(self) :
        return self.__tank.isDead()

