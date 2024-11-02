from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer

life = 4
record_score = 0
score = 0

class Herou(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed

        self.rect = self.image.get_rect()

        self.rect.y = rect_y
        self.rect.x = rect_x
        self.widht = rect_x
        self.heigh = rect_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Herou):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < self.widht + 600:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < self.heigh + 400:
            self.rect.y += self.speed




class Enemy(Herou):
    def update(self):
        global score
        global record_score
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0, win_widht - 150)
            score = score + 1
            record_score = record_score + 1



win_widht = 700
win_height = 500
window = display.set_mode((win_widht, win_height))
background = scale(load('pixil-frame-0.png'), (win_widht, win_height))



hero = Player('enemy.png', 200, (win_height) - 90,6, 50, 50)

monsters = sprite.Group()

for i in range(6):
    enemy = Enemy('push.png', randint(1, win_widht - 90), randint(1, win_height - 350), randint(4, 7), 50, 50)
    monsters.add(enemy)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont("Aril", 60)
font2 = font.SysFont("Aril", 32)
font3 = font.SysFont("Aril", 32)
font4 = font.SysFont("Aril", 32)
font5 = font.SysFont("Aril", 60)

txt_lose = font1.render("ЛОХ", True, (255,0,0))

while game:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

    if not finish:

        window.blit(background, (0, 0))
        monsters.draw(window)
        hero.reset()
        txt_score_lost = font2.render(f'Очки: {score}', True, (255, 255, 255))
        txt_record_score = font3.render(f'Рекорд: {record_score}', True, (255, 255, 255))
        txt_life = font4.render(f'Життя: {life}', True, (255, 255, 255))
        window.blit(txt_record_score, (0, 30))
        window.blit(txt_life, (win_widht - 125, 10))
        window.blit(txt_score_lost, (10, 50))

        monsters.update()
        hero.update()
        if sprite.spritecollide(hero, monsters, False):
            window.blit(txt_lose, (230, 230))

            finish = True
    if life <= 0:
        game = False

    elif finish == True and life > 0:
        score = 0
        life = life - 1
        finish = False
        time.delay(3000)
        for m in monsters:
            m.kill()

        for i in range(6):
            enemy = Enemy('push.png', randint(1, win_widht - 90), randint(1, win_height - 350), randint(4, 6), 50, 50)
            monsters.add(enemy)





    display.update()
    clock.tick(FPS)









