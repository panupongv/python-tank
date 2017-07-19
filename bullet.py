import constants as setting
import sys,os
import pygame


class Bullet (pygame.sprite.Sprite) :
    def __init__( self, owner_id, x, y, direction, image_path ,bullet_damage,bullet_speed, mana_reduct) : #add to bullet group
        super(Bullet, self).__init__()
        self.rect = self.__createBulletRect(image_path)
        
        #static contant initialize
        self.__bullet_damage = bullet_damage
        self.__bullet_speed = bullet_speed
        self.__mana_reduction = mana_reduct
        self.radius = 5
        
        self.__owner_id = owner_id

        self.__setStartPosition( x, y )

        self.__setSpeed( direction )

    def __setStartPosition( self, x, y ) :
        self.rect.x = x*setting.GRID_SIZE
        self.rect.y = y*setting.GRID_SIZE
        
    def __createBulletRect( self , image_path ) :
        path = os.path.join(image_path)
        try :
            image = pygame.image.load(path)
        except :
            print('cannot load image from path :', path)
            raise

        #may have to set color transparent key
        surface = image.convert()

        return surface.get_rect()
    
    def __setSpeed( self, direction ) :
        x,y = 0,0
        
        if direction == 'down' :
            y = 1
        elif direction == 'up' :
            y = -1
        elif direction == 'left' :
            x = -1
        elif direction == 'right' :
            x = 1
        else :
            raise
        
        self.__speed_x = self.__bullet_speed*x
        self.__speed_y = self.__bullet_speed*y
        
    def isMakingContact ( self, tank ) :
        if self.__owner_id == bot.getId() :
            return False

        return pygame.sprite.collide(self, tank)

    def update( self, game ) :
        self.rect.x += self.__speed_x*game.deltaTime()
        self.rect.y += self.__speed_y*game.deltaTime()

        if self.__isOutOfMap() :
            self.kill()

    def __isOutOfMap( self ) :
        return self.rect.x > setting.SCREEN_WIDTH or self.rect.x < -10 or \
               self.rect.y > setting.SCREEN_HEIGHT or self.rect.y < -10

    def getDamage( self ) :
        return self.__bullet_damage

    def getManaReduction( self ):
        return self.__mana_reduction


class Bullet_Heal(Bullet):
    def __init__( self, owner_id, x, y, direction) :
        heal_path = ""
        super().__init__( self, owner_id, x, y, direction, heal_path ,-5, 35,20) #add


class Bullet_Damage(Bullet):
    def __init__( self, owner_id, x, y, direction) :
        damage_path = ""
        super().__init__( self, owner_id, x, y, direction, heal_path ,10,50,10) #add

        
