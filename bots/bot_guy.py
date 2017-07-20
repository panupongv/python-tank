import pygame

from core.tank import TankPrototype

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
        print("update guy")
                        
    # return direction if in range , return None if not in range              
    def SuggestionFire(tank_me, tank_other):
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

        
            


            
