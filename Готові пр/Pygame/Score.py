import pygame.font
from gun import Gunsters
from pygame.sprite import Group
class Scores():
    "Рекорди"
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (100, 130, 50)
        self.font = pygame.font.SysFont(None, 26)
        self.score_draw()
        self.image_hight_score()
        self.image_guns()
    def score_draw(self):
        "показує рекорд"
        self.score_draw = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_draw.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_guns(self):
        self.guns = Group()
        for gun_nubmer in range(self.stats.gun_left):
            gun = Gunsters(self.screen)
            gun.rect.x = 15 + gun_nubmer * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)


    def image_hight_score(self):

        self.hight_score_image = self.font.render(str(self.stats.hight_score), True, self.text_color, (0, 0, 0))
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.screen_rect.top + 20

    def show_score(self):
        "Вивід рекорду на екран"
        self.screen.blit(self.score_draw, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.guns.draw(self.screen)
