import pygame, random                         # 1. Importamos pygame
from pygame.sprite import Sprite         # 2. Despues Sprite

from game.utils.constants import ENEMY_1, SCREEN_WIDTH, SCREEN_HEIGHT     # Y cuando sea necesario importamos mas metodos, atributos o variables

speedy = 10

class Enemy(Sprite):     # 3. Creamos la clase
    
    def __init__(self):      # 4. Su constructor

        self.image_size = (70, 90)
        
        self.image = pygame.transform.scale(ENEMY_1, self.image_size)

        self.image_rect = self.image.get_rect()                          # 5. Sus atributos
        
        self.image_rect.x = (SCREEN_WIDTH / 2) - (self.image_size[0] / 2)
        self.image_rect.y = self.image_size[1]
        
        self.speed_x = 5
        self.speed_y = 5

    
    def update(self):  
        
        self.enemy_1()        # 6. Un metodo update


    def enemy_1(self):

        self.image_rect.x += self.speed_x
        self.image_rect.y += self.speed_y

        if (self.image_rect.x > (SCREEN_WIDTH - 70) or self.image_rect.x < 0):
            self.speed_x *= -1    
        if self.image_rect.y > (SCREEN_HEIGHT - 90) / 3:              #Nave grande que robote hasta la mitad del eje Y y en los limites del eje X
            self.speed_y *= -1
        if self.image_rect.y < 0:
            self.speed_y *= -1