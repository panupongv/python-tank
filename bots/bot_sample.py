import pygame

from core.tank import TankPrototype

class BotSample ( TankPrototype ):
    #because this bot class is inherited from TankPrototype class
    #this class will derive and obtain all public methods available in TankPrototype
    #the methods available for use listed below
    '''
    getHP()                get current HP
    getMP()                get current MP
    getName()              get name
    getPosition()          get x, y position
    isMoving()             check if moving( can't change direction while moving )
    getTankInfoList()      get a list of tank information
    isAtEdge(direction)    check if at edge of bettle field
    getDirection()         get heading direction ( also moving directiohn if is moving )
    isAlly(another_bot)    check if another_bot is an alliance or not
    getTeamColor()         get current team color
    readyToMove()          check if ready to move ( also check cooldown and mana cost )
    readyToShoot()         check if ready to shoot ( also check cooldown and mana cost )
    move(direction)        move forward in the specified direction ('left' 'right' 'up' 'down')
    shoot(direction)       fire a bullet in the specified direction ('left' 'right' 'up' 'down') : cost ?? mana
    shoot_heal(direction)  fire a potion in the specified direction ('left' 'right' 'up' 'down') : cost ?? mana
    '''
    
    def start( self ) :
        #this method will be call at the __init__() function of a super class
        #use this to create and initialize variable you will use in your tank algorithm
        self.current_direction = 'left'
    
    def update( self ) :
        #this method will be called every millisecond
        #code your algorithm here and it will affect your tank action
        
        '''change current_direction when this tank is at the edge of the battle field'''
        if self.isAtEdge(self.current_direction) :
            if self.current_direction == 'left' :
                self.current_direction = 'right'
            elif self.current_direction == 'right' :
                self.current_direction = 'left'
                
        '''then move it to the determined direction'''
        self.move(self.current_direction)
        
        '''get enemy list from method .getEnemyList()'''
        enemy_list = self.getEnemyList()
                
        '''then we check for any enemy locate in the same column and shoot it'''
        for enemy in enemy_list :
            self_x, self_y = self.getPosition()
            enemy_x, enemy_y = enemy.getPosition()
            
            if self_x == enemy_x :      #if on the same column
                if enemy_y < self_y :   #enemy is located above
                    self.shoot('up')
                else :                  #enemy is located below
                    self.shoot('down')
  
