import pygame

from constants import *

class Tank(pygame.sprite.Sprite):
    def __init__(self, team, id_tag, color, x, y, direction, *group):
        super(Tank, self).__init__(*group)
        self.__team = team
        self.__tag = id_tag
        self.images = [pygame.image.load(color + "_tank_left.png"),
                       pygame.image.load(color + "_tank_right.png"),
                       pygame.image.load(color + "_tank_up.png"),
                       pygame.image.load(color + "_tank_down.png"),]
        self.__direction = direction
        self.image = self.images[self.__getIndex()]
        self.rect = self.image.get_rect()
        
        self.__grid_x = x
        self.__grid_y = y
            
    def update(self, game):
        self.__right()
        self.rect.x = self.__grid_x * BLOCK_SIZE
        self.rect.y = self.__grid_y * BLOCK_SIZE

    def __left(self):
        if self.__grid_x > 0:
            self.__grid_x -= 1
        self.image = self.images[0]
    def __right(self):
        if self.__grid_x < 9:
            self.__grid_x += 1
        self.image = self.images[1]
    def __up(self):
        if self.__grid_y > 0:
            self.__grid_x -= 1
        self.image = self.images[2]
    def __down(self):
        if self.__grid_y < 9:
            self.__grid_x += 1
        self.image = self.images[3] 
    
    def getID(self):
        return self.__tag

    def getPosition(self):
        return self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE

    def __getIndex(self):
        if self.__direction == "left": return 0
        if self.__direction == "right": return 1
        if self.__direction == "up": return 2
        if self.__direction == "down": return 3

  
