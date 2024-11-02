import pygame
from pygame.sprite import Sprite

class Gunsters(Sprite):
    def __init__(self, screen):
        super(Gunsters, self). __init__()
        self.screen = screen
        self.image = pygame.image.load("Image/pixilart-drawing.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self):
        "малювка"
        self.screen.blit(self.image, self.rect)
    def update(self):
        "Обновка позиций пушки"
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.7
        if self.mleft and self.rect.left > 0:
            self.center -= 0.7
        self.rect.centerx = self.center
    def create_gun(self):

        self.center = self.screen_rect.centerx