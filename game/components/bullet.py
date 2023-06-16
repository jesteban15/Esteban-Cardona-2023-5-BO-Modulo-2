
import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET, SCREEN_WIDTH

class Bullet(Sprite):

    def __init__(self, spaceship_center):
        super().__init__()        
        self.image = pygame.transform.scale(BULLET, (10, 20))
        self.image_rect = self.image.get_rect() 
        self.speed = 15
        self.rect.center = spaceship_center

    def update(self):
        self.rect.y -= self.speed 
        if self.rect.y < 0 or self.rect.y > SCREEN_WIDTH:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))