import pygame

from core.tank import TankPrototype

class BotSample ( TankPrototype ):
    #because this bot class is inherited from TankPrototype class
    #this class will derive and obtain all public methods available in TankPrototype
    #the methods available for use listed below
    '''
    getHP()                get current HP
    getMP()                get current MP
    isAlly(another_bot)    check if another_bot is an alliance or not
    getTeamColor()         get current team color
    readyToMove()          check if ready to move ( cooldown and mana cost )
    readyToShoot()         check if ready to shoot ( cooldown and mana cose )
    shoot(direction)       fire a bullet in the specified direction ('left' 'right' 'up' 'down') : cost ?? mana
    heal(direction)        fire a potion in the specified direction ('left' 'right' 'up' 'down')
    '''
    def start( self ) :
        self.current_direction = 'left'
    
    def update( self ) :
        #code your algorithm here        
        if self.isAtEdge(self.current_direction) :
            if self.current_direction == 'left' :
                self.current_direction = 'right'
            elif self.current_direction == 'right' :
                self.current_direction = 'left'
                
        self.move(self.current_direction)
        
        tank_list = self.getTankInfoList()
        ally_list = []
        enemy_list = []
        
        for tank in tank_list :
            if tank.isAlly(self) and not tank.isMySelf(self) :
                ally_list.append(tank)
            elif tank.isAlly(self) == False :
                enemy_list.append(tank)
                
        for enemy in enemy_list :
            if enemy.getPosition()[0] == self.getPosition()[0]:
                if enemy.getPosition()[1] < self.getPosition()[0] :
                    self.shoot('up')
                else :
                    self.shoot('down')
  
