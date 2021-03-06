import pygame
import random

from core.tank import TankPrototype
from core.constants import *

class BotGuy ( TankPrototype ):
    #because this bot class is inherited from TankPrototype class
    #this class will derive and obtain all public methods available in TankPrototype
    #the methods available for use listed below
    '''
    getHP()                get current HP
    getMP()                get current MP
    getName()              get name
    getPosition()          get x, y position
    isMoving()             check if moving( cant move while moving )
    getTankInfoList()      get a list of tank information
    isAtEdge(direction)    check if at edge of bettle field
    getDirection()         get heading direction ( also moving directiohn if is moving )
    isAlly(another_bot)    check if another_bot is an alliance or not
    getTeamColor()         get current team color
    readyToMove()          check if ready to move ( cooldown and mana cost )
    readyToShoot()         check if ready to shoot ( cooldown and mana cose )
    move(direction)
    shoot(direction)       fire a bullet in the specified direction ('left' 'right' 'up' 'down') : cost ?? mana
    heal(direction)        fire a potion in the specified direction ('left' 'right' 'up' 'down')
    '''

    # change to shoot heal
    
    def start( self ) :
        #this method will be call at the beginning once
        #use this to initialize variable you will use in your tank algorithm
        self.current_direction = 'left'
    
    def update( self ) :
        #Op method dat will reck ya enemy
        command = random.randint(0,3)

        if(command):
            if(self.getMP() > MAX_MP // 2):
                self.updateShoot()
            else:
                self.updateMove()
        else:
            self.updateMove()


    def updateShoot(self):
        if (self.readyToShoot()):
            for tank in self.getEnemyList():
                direction = self.SuggestionFire(self, tank)
                if (direction == 'none'):
                    continue
                else:
                    if (self.isAlly(tank)):
                        self.shoot(direction)
                    '''
                    else:
                        self.shoot(direction)
                    '''
        elif (self.readyToMove()):
            movementSet = ('left', 'right', 'up', 'down')
            while (True):
                direc = movementSet[random.randint(0, 3)]
                if (not self.isAtEdge(direc)):
                    self.move(direc)
                    break

    def updateMove(self):
        if (self.readyToMove()):
            movementSet = ('left', 'right', 'up', 'down')
            while (True):
                direc = movementSet[random.randint(0, 3)]
                if (not self.isAtEdge(direc)):
                    self.move(direc)
                    break
        elif (self.readyToShoot()):
            for tank in self.getEnemyList():
                direction = self.SuggestionFire(self, tank)
                if (direction == 'none'):
                    continue
                else:
                    if (self.isAlly(tank)):
                        self.shoot(direction)
                    '''
                    else:
                        self.shoot(direction)
                    '''

                        
    # return direction if in range , return None if not in range              
    def SuggestionFire(self,tank_me, tank_other):
        x_other , y_other = tank_other.getPosition()
        x_me , y_me = tank_me.getPosition()
        
        if(abs(x_me - x_other) <= 2):
            if(y_me > y_other):
                return 'up'
        
            elif(y_me < y_other):
                return 'down'

        elif(abs(y_me - y_other) <= 2):
            if(x_me > x_other):
                return 'left'
        
            elif(x_me < x_other):
                return 'right'
            
        return 'none'
