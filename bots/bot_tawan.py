import pygame

from core.tank import TankPrototype

class BotTawan ( TankPrototype ):
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
        #this method will be called every millisecond
        #code your algorithm here and it will effect your tank action
        
        '''change direction when this tank is at the edge of the battle field'''
        if not self.canMove(self.current_direction) :
            if self.current_direction == 'left' :
                self.current_direction = 'right'
            elif self.current_direction == 'right' :
                self.current_direction = 'left'
                
        '''then move it to the determined direction'''
        self.move(self.current_direction)
        
        '''we can get the information of all the tanks in the field from getTankInfoList() method'''
        tank_list = self.getTankInfoList()
        
        '''the info list obtained is mixed with ally and enemy ( including yourself )'''
        '''it is not a bad idea to classify it first'''
        ally_list = []
        enemy_list = []
        for tank in tank_list :
            if tank.isAlly(self) and not tank.isMySelf(self) :
                ally_list.append(tank)
            elif tank.isAlly(self) == False :
                enemy_list.append(tank)
                
        '''then we check where the enemies are and shoot them'''
        for enemy in enemy_list :
            self_x, self_y = self.getPosition()
            enemy_x, enemy_y = enemy.getPosition()
            
            if self_x == enemy_x :      #if on the same column
                if enemy_y < self_y :   #enemy is located above
                    self.shoot('up')
                else :                  #enemy is located below
                    self.shoot('down')
  
