import pygame

class Enemy(pygame.sprite.Sprite):


    def __init__(self, screen):
        "Позиция"
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.05
        self.rect.y = self.y





