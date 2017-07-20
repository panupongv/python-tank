import pygame

from core.constants import *
from core.bullet import Bullet_Heal, Bullet_Damage
from core.bar import Bar

class TankPrototype (pygame.sprite.Sprite):
    #constructor
    def __init__(self, game, name, team_color, x, y, direction, *group):
        super().__init__(*group)

        self.__hp = Bar(RED, MAX_HP, MAX_HP, x * BLOCK_SIZE, y * BLOCK_SIZE) 
        self.__mp = Bar(BLUE, MAX_MP, MAX_MP, x * BLOCK_SIZE, y * BLOCK_SIZE + BAR_HEIGHT)
        
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

        self.__shoot_cooldown = SHOOT_COOLDOWN
        self.__move_cooldown = MOVE_COOLDOWN

        game.add_hidden_update(self.__hidden_update)
        self.__game = game

    #private methods ( internal use only, other cant use it, it's danger to allow so )
    def __checkBulletCollision(self):
        for bullet in self.__game.bullet_list:
            if bullet.isMakingContact(self):
                self.__hp -= bullet.getDamage()
                bullet.kill()
                if self.__hp <= 0:
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
        if self.__direction == "left": return 0
        if self.__direction == "right": return 1
        if self.__direction == "up": return 2
        if self.__direction == "down": return 3

    def __hidden_update(self):
        self.__move_cooldown -= 1 / FPS
        self.__shoot_cooldown -= 1 / FPS
        self.__mp += MP_REGEN_RATE / FPS
    
        self.rect.x = self.__grid_x * BLOCK_SIZE
        self.rect.y = self.__grid_y * BLOCK_SIZE

        self.__hp.updatePosition(self.rect.x, self.rect.y)
        self.__mp.updatePosition(self.rect.x, self.rect.y + BAR_HEIGHT)

        self.__checkBulletCollision()

    #public methods
    def getHP(self):
        return int(self.__hp)

    def getMP(self):
        return int(self.__mp)

    def isAlly(self, tank):
        return self.__team_color == tank.getTeamColor()

    def getTeamColor(self):
        return self.__team_color

    def readyToMove(self):
        return self.__move_cooldown <= 0

    def readyToShoot(self):
        return self.__shoot_cooldown <= 0
            
    def move(self, direction) :
        if not self.readyToMove() :
            return

        if direction == 'left' :
            self.__grid_x -= 1
            self.image = self.images[0]
            
        elif direction == 'right' :
            self.__grid_x += 1
            self.image = self.images[1]
            
        elif direction == 'up' :
            self.__grid_y -= 1
            self.image = self.images[2]
            
        elif direction == 'down' :
            self.__grid_y += 1
            self.image = self.images[3]
        else :
            raise ValueError('unknown direction given : ' + str(direction))

        self.__clamp_grid_pos()
        self.__resetMoveCooldown()

    def shoot(self, direction):
        if self.readyToShoot() and self.__mp - DAMAGE_BULLET_MANA_COST >= 0:
            bullet = Bullet_Damage(self, direction, self.__game.sprite_list, self.__game.bullet_list)
            self.__resetShootCooldown()
            self.__mp -= DAMAGE_BULLET_MANA_COST

    def heal(self, direction):
        if self.readyToShoot() and self.__mp - HEAL_BULLET_MANA_COST >= 0:
            bullet = Bullet_Heal(self, direction, self.__game.sprite_list, self.__game.bullet_list)
            self.__resetShootCooldown()
            self.__mp -= HEAL_BULLET_MANA_COST
            
    def getName(self):
        return self.__name

    def getPosition(self):
        return self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE

    #for calling bars.draw() from main
    def drawBars(self, screen):
        self.__hp.draw(screen)
        self.__mp.draw(screen)
        
    #this is pseudo abstract method ( should be override )
    #the update process that should not be invoked from outside is in hidden_update() method
    def update(self):
        pass

  
