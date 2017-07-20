import pygame
from math import *

from core.tank import TankPrototype

class BotEit ( TankPrototype ):
    #because this bot class is inherited from TankPrototype class
    #this class will derive and obtain all public methods available in TankPrototype
    #the methods available for use listed below
    '''
    getHP()                get current HP
    getMP()                get current MP
    getName()              get name
    getPosition()            get x, y position
    isMoving()               check if moving( cant move while moving )
    getTankInfoList()       get a list of tank information
    isAtEdge(direction)       check if at edge of bettle field
    getDirection()           get heading direction ( also moving directiohn if is moving )
    isAlly(another_bot)    check if another_bot is an alliance or not
    getTeamColor()         get current team color
    readyToMove()          check if ready to move ( cooldown and mana cost )
    readyToShoot()         check if ready to shoot ( cooldown and mana cose )
    move(direction)
    shoot(direction)       fire a bullet in the specified direction ('left' 'right' 'up' 'down') : cost ?? mana
    heal(direction)        fire a potion in the specified direction ('left' 'right' 'up' 'down')
    '''
    
    def start( self ) :
        #this method will be call at the beginning once
        #use this to initialize variable you will use in your tank algorithm
        self.x, self.y = self.getPosition()
        self.cloest_enemy = None
        
    def move_to_tank( self, target_tank):
        enemy_x, enemy_y = target_tank.getPosition()
        if self.x < enemy_x:
            self.move("right")
        elif self.x > enemy_x:
            self.move("left")
        elif self.x == enemy_x:
            if self.y < enemy_y:
                self.move("down")
            elif self.y > enemy_y:
                self.move("up")

    def which_is_closer( self, tank1, tank2):
        tank1_x, tank1_y = tank1.getPosition()
        tank2_x, tank2_y = tank2.getPosition()

        distance_to_tank1 = sqrt(abs(self.x-tank1_x)**2 + abs(self.y-tank1_y)**2)
        distance_to_tank2 = sqrt(abs(self.x-tank2_x)**2 + abs(self.y-tank2_y)**2)

        if distance_to_tank1 < distance_to_tank2:
            return tank1
        else:
            return tank2
        
    def set_closet_enemy( self, enemy_list ):
        for enemy in enemy_list:
            if self.cloest_enemy == None or not self.cloest_enemy in enemy_list:
                self.cloest_enemy = enemy
                continue
            self.cloest_enemy = self.which_is_closer(enemy,self.cloest_enemy)
            
        
    
    def update( self ) :
        #this method will be called every millisecond
        #code your algorithm here and it will effect your tank action

        self.x, self.y = self.getPosition()
        
        '''the info list obtained is mixed with ally and enemy ( including yourself )'''
        '''it is not a bad idea to classify it first'''
        ally_list = self.getAllyList()
        enemy_list = self.getEnemyList()
                
        self.set_closet_enemy(enemy_list)
        self.move_to_tank(self.cloest_enemy)
        cloest_x,cloest_y = self.cloest_enemy.getPosition()
#        print(self.cloest_enemy.getName())
        #print(len(enemy_list))
        if self.x == cloest_x :      
            if self.y > cloest_y :   #enemy is located above
                self.shoot('up')
            else :                  #enemy is located below
                self.shoot('down')
        
        
        if self.y == cloest_y:
            if self.x > cloest_x:
                self.shoot('left')
            else:
                self.shoot('right')
                
