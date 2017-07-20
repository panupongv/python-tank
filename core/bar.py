import pygame
import core.constants as setting

class Bar:
    def __init__(self, color, initial_val, max_val, x, y):
        self.__color = color

        if initial_val > max_val:
            initial_val = max_val
        self.__val = initial_val
        self.__MAX_VAL = max_val

        self.__x = x
        self.__y = y

    def updatePosition(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, val):
        self.__val += val
        if self.__val > self.__MAX_VAL:
            self.__val = self.__MAX_VAL
        return Bar(self.__color, self.__val, self.__MAX_VAL, self.__x, self.__y)

    def __sub__(self, val):
        self.__val -= val
        return Bar(self.__color, self.__val, self.__MAX_VAL, self.__x, self.__y)

    def __lt__(self, val):
        return self.__val < val

    def __le__(self, val):
        return self.__val <= val

    def __eq__(self, val):
        return self.__val == val

    def __ne__(self, val):
        return self.__val != val

    def __gt__(self, val):
        return self.__val > val

    def __ge__(self, val):
        return self.__val >= val

    def getValue(self):
        return self.__val
    
    def draw(self, screen):
        pygame.draw.rect(screen, setting.BLACK, (self.__x, self.__y, setting.BLOCK_SIZE, setting.BAR_HEIGHT))
        if self.__val > 0:
            pygame.draw.rect(screen, self.__color, (self.__x, self.__y, self.__val / self.__MAX_VAL * setting.BLOCK_SIZE, setting.BAR_HEIGHT))
