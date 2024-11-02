import pygame, controls
import sys
from gun import Gunsters
from pygame.sprite import Group
from stats import Stats
from Score import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    bg_color = (0, 0, 0)
    gun = Gunsters(screen)
    bullets = Group()
    enemys = Group()
    controls.create_army(screen, enemys)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
            controls.events(screen, gun, bullets)
            if stats.run_game:

                gun.update()

                controls.update(bg_color, screen, stats, sc, gun, enemys, bullets)
                controls.update_bullets(screen, stats, sc, enemys, bullets)
                controls.update_enemy(stats, screen, sc, gun, enemys, bullets)


run()