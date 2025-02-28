import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullet import  Bullet


# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite
MOVE = 5
# spaceship tiene una "imagen"
class SpaceShip(Sprite):
    
    def __init__(self):

        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 300 #(SCREEN_WIDTH / 2) - (self.image_size[0] / 2)  #Ponemos la nave en el centro y parte inferior
        self.image_rect.y = 500 #SCREEN_HEIGHT - self.image_size[1] - 20
        self.bullet = None
               
    def update(self):
               #Definimos las caracteristicas de movimiento
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.image_rect.x -= MOVE
            if self.image_rect.x < -45:
               self.image_rect.x += SCREEN_WIDTH              
        if pressed[pygame.K_RIGHT]:
            self.image_rect.x += MOVE
            if self.image_rect.x > SCREEN_WIDTH:
               self.image_rect.x -= SCREEN_WIDTH
        if pressed[pygame.K_UP]:
            self.image_rect.y -= MOVE
            if self.image_rect.y < 0:
                self.image_rect.y += SCREEN_HEIGHT
        if pressed[pygame.K_DOWN]:
            self.image_rect.y += MOVE
            if self.image_rect.y > SCREEN_HEIGHT:
                self.image_rect.y = 0 
        
        if self.bullet is not None:
           self.bullet.update()
  
    def shoot(self):
        self.bullet = Bullet(self.image_rect.center)
       
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)

        if self.bullet is not None:
            self.bullet.draw(screen)