import constants as setting
import sys,os
import pygame

class Bullet (pygame.sprite.Sprite) :
    def __init__( self, tank, direction, image_path ,bullet_damage,bullet_speed, *group) : #add to bullet group
        super(Bullet, self).__init__(*group)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        
        #static contant initialize
        self.__bullet_damage = bullet_damage
        self.__setSpeed( direction, bullet_speed )
        self.radius = 5
        
        self.__owner_name = tank.getName()

        x, y = tank.getPosition()
        self.__setStartPosition( x, y )



    def __setStartPosition( self, x, y ) :
        self.rect.x = x*setting.BLOCK_SIZE + setting.BLOCK_SIZE / 2 - self.rect.width / 2
        self.rect.y = y*setting.BLOCK_SIZE + setting.BLOCK_SIZE / 2 - self.rect.height / 2
        
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
    
    def __setSpeed( self, direction, bullet_speed ) :
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
        
        self.__speed_x = bullet_speed*x
        self.__speed_y = bullet_speed*y
        
    def isMakingContact ( self, tank ) :
        if self.__owner_name == tank.getName() :
            return False

        return pygame.sprite.collide(self, tank)

    def update( self, game ) :
        self.rect.x += self.__speed_x/setting.FPS#*game.getDeltaTime()
        self.rect.y += self.__speed_y/setting.FPS#*game.getDeltaTime()
        print(self.rect.x, self.rect.y)
        if self.__isOutOfMap() :
            self.kill()

    def __isOutOfMap( self ) :
        return self.rect.x > setting.SCREEN_WIDTH or self.rect.x < -10 or \
               self.rect.y > setting.SCREEN_HEIGHT or self.rect.y < -10

    def getDamage( self ) :
        return self.__bullet_damage


class Bullet_Heal(Bullet):
    def __init__( self, tank, direction, *group) :
        heal_path = ""
        super().__init__( tank, direction, "bullet.png" ,-5, 60, *group) #add


class Bullet_Damage(Bullet):
    def __init__( self, tank, direction, *group) :
        damage_path = ""
        super().__init__( tank, direction, "bullet.png" , 10, 180, *group) #add

        
