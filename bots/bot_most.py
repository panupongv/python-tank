import pygame
import random

from core.tank import TankPrototype

class BotMost ( TankPrototype ):
    def start( self ) :
        self.current_move_direction = 'left'
        self.current_x, self.current_y = self.getPosition()
        self.corner_x = self.corner_y = 0
        self.move_directions = ["", ""]
        self.shoot_directions = ["", ""]
        self.counter = 0
        
        if self.current_x <= 4:
            self.corner_x = 0
            self.move_directions[0] = "left"
            self.shoot_directions[0] = "right"
        else:
            self.corner_x = 9
            self.move_directions[0] = "right"
            self.shoot_directions[0] = "left"
        if self.current_y <= 4:
            self.corner_y = 0
            self.move_directions[1] = "up"
            self.shoot_directions[1] = "down"
        else:
            self.corner_y = 9
            self.move_directions[1] = "down"
            self.shoot_directions[1] = "up"

    def __inCorner(self):
        return self.current_x == self.corner_x and \
               self.current_y == self.corner_y
    
    def update( self ) :
        self.current_x, self.current_y = self.getPosition()
        if not self.__inCorner():
            if self.current_x != self.corner_x:
                self.move(self.move_directions[0])
            elif self.current_y != self.cornert_y:
                self.move(self.move_directions[1])
        else:
            for enemy in self.getEnemyList():
                enemy_x, enemy_y = enemy.getPosition()
                self.__shoot(enemy_x, enemy_y)

        self.counter = (self.counter + 1) % 2

    def __shoot(self, enemy_x, enemy_y):
        if self.counter == 0:
            if self.current_x == enemy_x:
                self.shoot(self.shoot_directions[1])
            elif self.current_y == enemy_y:
                self.shoot(self.shoot_directions[0])
        else:
            if self.current_y == enemy_y:
                self.shoot(self.shoot_directions[0])
            elif self.current_x == enemy_x:
                self.shoot(self.shoot_directions[1])
        
            
            
        
        
  
