import pygame
import random

from core.tank import TankPrototype

class FuckBot420 ( TankPrototype ):
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
        self.current_direction = 'left'
    
    def update( self ) :
        self_x, self_y = self.getPosition()
        choice = random.randint(0, 3)
        choice2 = random.randint(0, 3)
        if (self.isAtEdge(self.current_direction) or self.isBlocked(self.current_direction) ) or choice * choice2 == 9:
            if self.current_direction == 'left' :
                if choice == 2:
                    self.current_direction = 'right'  
                elif choice == 1:
                    self.current_direction = 'down'
                else:
                    self.current_direction = 'up'
                    
            elif self.current_direction == 'right' :
                if choice == 2:
                    self.current_direction = 'left'  
                elif choice == 1:
                    self.current_direction = 'down'
                else:
                    self.current_direction = 'up'
                    
            elif self.current_direction == 'up' :
                if choice == 2:
                    self.current_direction = 'down'  
                elif choice == 1:
                    self.current_direction = 'right'
                else:
                    self.current_direction = 'left'
                    
            elif self.current_direction == 'down' :
                if choice == 2:
                    self.current_direction = 'up'  
                elif choice == 1:
                    self.current_direction = 'right'
                else:
                    self.current_direction = 'left'
    
        self.move(self.current_direction)
        
        enemy_list = self.getEnemyList()
        for enemy in enemy_list :
            enemy_x, enemy_y = enemy.getPosition()
            
            if self.current_direction == 'left' or self.current_direction == 'right':
                if abs(self_x - enemy_x <= 1):
                    if enemy_y >= self_y:
                        self.shoot('down')
                    else:
                        self.shoot('up')
            elif self.current_direction == 'up' or self.current_direction == 'down':
                if abs(self_y - enemy_y <= 1):
                    if enemy_x >= self_x:
                        self.shoot('right')
                    else:
                        self.shoot('left')
  
