import pygame, random                         # 1. Importamos pygame
from pygame.sprite import Sprite         # 2. Despues Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT     # Y cuando sea necesario importamos mas metodos, atributos o variables

speedy = 10

class Enemy(Sprite):     # 3. Creamos la clase
    
    def __init__(self):      # 4. Su constructor

        self.image_size = (70, 90)
        self.image_size2 = (30, 50)
        self.image_size3 = (30, 50)
        self.image_size4 = (30, 50)
        
        self.image = pygame.transform.scale(ENEMY_1, self.image_size)
        self.image2 = pygame.transform.scale(ENEMY_2, self.image_size2)
        self.image3 = pygame.transform.scale(ENEMY_2, self.image_size3)
        self.image4 = pygame.transform.scale(ENEMY_2, self.image_size4)

        self.image_rect = self.image.get_rect() 
        self.image_rect2 = self.image2.get_rect()   
        self.image_rect3 = self.image3.get_rect()
        self.image_rect4 = self.image4.get_rect()
                                                                                         # 5. Sus atributos
        self.image_rect.x = (SCREEN_WIDTH / 2) - (self.image_size[0] / 2)
        self.image_rect.y = self.image_size[1]
        self.image_rect2.x = random.randrange(SCREEN_WIDTH)
        self.image_rect2.y = random.randrange(-10, 10)
        self.image_rect3.x = random.randrange(SCREEN_WIDTH)
        self.image_rect3.y = random.randrange(-10, 10)
        self.image_rect4.x = random.randrange(SCREEN_WIDTH)
        self.image_rect4.y = random.randrange(-10, 10)
        
        self.speed_x = 5
        self.speed_y = 5
        self.speed_x1 = speedy
        self.speed_y1 = speedy
        self.speed_x2 = speedy
        self.speed_y2 = speedy
        self.speed_x3 = speedy
        self.speed_y3 = speedy
    
    def update(self):  
        self.enemy_1()      
        self.enemy_2()    
        self.enemy_3()    # 6. Un metodo update
        self.enemy_4()

    def enemy_1(self):

        self.image_rect.x += self.speed_x
        self.image_rect.y += self.speed_y

        if (self.image_rect.x > (SCREEN_WIDTH - 70) or self.image_rect.x < 0):
            self.speed_x *= -1    
        if self.image_rect.y > (SCREEN_HEIGHT - 90) / 3:              #Nave grande que robote hasta la mitad del eje Y y en los limites del eje X
            self.speed_y *= -1
        if self.image_rect.y < 0:
            self.speed_y *= -1

    def enemy_2(self):

        self.image_rect2.x += self.speed_x1
        self.image_rect2.y += self.speed_y1

        if self.image_rect2.x > (SCREEN_WIDTH - 30) or self.image_rect2.x < 0:
            self.speed_x1 *= -1    
        if self.image_rect2.y > SCREEN_HEIGHT - 50:               #Mini nave que rebota en cada limite de los ejes
            self.speed_y1 *= -1
        if self.image_rect2.y < 0:
            self.speed_y1 *= -1

    def enemy_3(self):

        self.image_rect3.x += self.speed_x2
        self.image_rect3.y += self.speed_y2

        if self.image_rect3.x > (SCREEN_WIDTH - 30) or self.image_rect3.x < 0:
               self.speed_x2 *= -1   
        if self.image_rect3.y < 0:                                                      #Mini nave que rebota en eñ eje X y traspasa eje Y
                self.image_rect3.y += SCREEN_HEIGHT
        if self.image_rect3.y > SCREEN_HEIGHT:
                self.image_rect3.y = 0

    def enemy_4(self):
         
        self.image_rect4.x += self.speed_x3
        self.image_rect4.y += self.speed_y3

        if self.image_rect4.x < 0:
               self.image_rect4.x += SCREEN_WIDTH
        if self.image_rect4.x > SCREEN_WIDTH:
               self.image_rect4.x -= SCREEN_WIDTH          #Mini nave que rebota en eje Y y traspasa eje X
        if self.image_rect4.y > SCREEN_HEIGHT - 50:
                self.speed_y3 *= -1
        if self.image_rect4.y < 0:
                self.speed_y3 *= -1
        

        

        
            


      




