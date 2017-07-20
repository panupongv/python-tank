from core.constants import *
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

        x, y = tank.rect.x + tank.rect.width/2, tank.rect.y + tank.rect.height/2
        self.__setStartPosition( x, y )

    def __setStartPosition( self, x, y ) :
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        
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

        return pygame.sprite.collide_rect(self, tank)

    def update(self) :
        self.rect.x += self.__speed_x/FPS
        self.rect.y += self.__speed_y/FPS
        if self.__isOutOfMap() :
            self.kill()

    def __isOutOfMap( self ) :
        return self.rect.x > SCREEN_WIDTH or self.rect.x < -10 or \
               self.rect.y > SCREEN_HEIGHT or self.rect.y < -10

    def getDamage( self ) :
        return self.__bullet_damage

class Bullet_Heal(Bullet):
    def __init__( self, tank, direction, *group) :
        damage = HEAL_BULLET_DAMAGE
        speed = HEAL_BULLET_SPEED
        super().__init__( tank, direction, "source/heart.png", damage, speed, *group) #add

class Bullet_Damage(Bullet):
    def __init__( self, tank, direction, *group) :
        damage = DAMAGE_BULLET_DAMAGE
        speed = DAMAGE_BULLET_SPEED
        super().__init__( tank, direction, "source/bullet.png", damage, speed, *group) #add

        
