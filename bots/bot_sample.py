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
    
    def update( self ) :
        #code your algorithm here        
        self.move('right')
        
        info_list = self.getTankInfoList()
        for info in info_list :
            if not self.isAlly(info) :
                if info.getPosition()[0] == self.getPosition()[0] :
                    self.shoot('down')

  
