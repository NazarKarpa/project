import pygame, sys
from Pul import Bullet
from enemy import Enemy
import time
def events(screen, gun, bullets):
    "Контроль евентов"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, enemys, bullets):

    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_pul()
    gun.output()
    enemys.draw(screen)

    pygame.display.flip()
def update_bullets(screen, stats, sc, enemys, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, enemys, True, True)
    if collision:
        for enemys in collision.values():
            stats.score += 10 * len(enemys)
            sc.show_score()
            check_score(stats, sc)
            sc.image_guns()
    if len(enemys) == 0:
        bullets.empty()
        create_army(screen, enemys)


def gun_kill(stats, screen, sc, gun, enemys, bullets):
    if stats.gun_left > 0:

        stats.gun_left -= 1
        sc.image_guns()
        enemys.empty()
        bullets.empty()
        create_army(screen, enemys)
        gun.create_gun()
        time.sleep(2)

    else:
        stats.run_game = False
        sys.exit()



def update_enemy(stats, screen, sc, gun, enemys, bullets):
    enemys.update()
    if pygame.sprite.spritecollideany(gun, enemys):
        gun_kill(stats, screen, sc, gun, enemys, bullets)
    enemys_check(stats, screen, sc, gun, enemys, bullets)

def enemys_check(stats, screen, sc, gun, enemys, bullets):
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, enemys, bullets)
            break
def create_army(screen, enemys):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    numbers_enemy_x = int((600 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    numbers_enemy_y = int((600 - 100 - 2 * enemy_height) / enemy_height)

    for row_number in range(numbers_enemy_y - 2):
        for enemy_nubmer in range(numbers_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_nubmer
            enemy.y = enemy_height + enemy_height * row_number

            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
            enemys.add(enemy)


def check_score(stats, sc):
    if stats.score > stats.hight_score:
        stats.hight_score = stats.score
        sc.image_hight_score()
        with open("hight_score.txt", "w") as f:
            f.write(str(stats.hight_score))




