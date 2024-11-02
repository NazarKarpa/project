#Імпорт часу шоб його визначати та бібліотеки пайгейм для створеня гри
import time
import pygame.locals
from pygame import *
#Імпорт рандому в нашій грі
from random import randint, choice
import os
import sys
init()
font.init()
mixer.init()

WIDTH, HEIGHT = 900,600 #Розширення екрану

bg = image.load('background-1.png')#Добавлення картинки та ставимо висота і тд
bg = transform.scale(bg, (WIDTH, HEIGHT))

record_time = 0 #Шоб визначати рекорд часу

player_image = image.load('car0.png')#Добавлення картинки та ставимо висота і тд
player_image = transform.scale(player_image, (50, 80))

button_image_again = image.load('again_1-removebg-preview.png')#Добавлення картинки

#Добавлення зображень кнопок та анімації їх
button_image_play = image.load('PlayButton.png')
button_image_play_anim = image.load('PlayButton – копія.png')
button_image_exit = image.load('Quit_button-removebg-preview.png')
button_image_exit_anim = image.load('Quit_button-removebg-preview – копія.png')
button_image_home = image.load('HomeButton.png')
button_image_setting = image.load('menu_2_2_2.png')
#Підставляємо картинки під висота і ширину
button_image_play_anim = transform.scale(button_image_play_anim, (300, 200))
button_image_play = transform.scale(button_image_play, (300, 200))
button_image_exit_anim = transform.scale(button_image_exit_anim, (250, 150))
button_image_exit = transform.scale(button_image_exit, (250, 150))
#Добавляем решту картинок
bost_image = image.load('boostmega-removebg-preview.png')

pause_image = image.load('PauseButton.png')

enemy_image2 = image.load('car-truck2.png')
enemy_image3 = image.load('car-truck4.png')
enemy_image4 = image.load('car-truck5.png')

enemys_images = [enemy_image2, enemy_image3, enemy_image4]#Список картинок ворогів

#В зміну закидуємо звук
bop_sound = mixer.Sound('b0dedd1433038be.mp3')
bop_sound.set_volume(0.3)

class GameSprite(sprite.Sprite): #Створення конструктуру
    def __init__(self, sprite_img, width, height, rect_x, rect_y, speed):
        super().__init__()
        #Тут ми надаємо характеристики для наших кнопок
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
        self.mask = mask.from_surface(self.image)

    def draw(self):
        #Тут ми відмальвуємо спрайт
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):


        if keys[K_d] and self.rect.x < 700:#Провірка натиску кнопки

            self.rect.x += self.speed#Рух
            self.image = transform.rotate(player_image, -10)
        elif keys[K_a] and self.rect.x > 150:#Провірка натиску кнопки
            self.rect.x -= self.speed
            self.image = transform.rotate(player_image, 10)#Тут ми робимо ефект анімації
        if keys[K_w] and self.rect.y > 50:#Провірка натиску кнопки
            self.image = transform.rotate(player_image, 0)#Тут ми зупиняємо ефект
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:#Провірка натиску кнопки
            self.image = transform.rotate(player_image, 0)#Тут ми зупиняємо ефект
            self.rect.y += self.speed

class Enemy(GameSprite):

    def update(self):

        if self.rect.y > -200:
            self.rect.y -= self.speed#Рух ворога

class Button(GameSprite):#Спеціальний класс для кнопок
    pass

def random_car():
    #Тут ми задаємо рандомну сторону дороги, і ми тут робимо ворогів
    rand_race = randint(1, 4)
    rand_y = randint(600, 800)
    rand_speed = randint(5, 6)
    enemy_image = choice(enemys_images)
    if rand_race == 1:
        enemy = Enemy(enemy_image, 50, 95, 210, rand_y, rand_speed)
    if rand_race == 2:
        enemy = Enemy(enemy_image, 50, 95, 350, rand_y, rand_speed)
    if rand_race == 3:
        enemy = Enemy(enemy_image, 50, 95, 500, rand_y, rand_speed)
    if rand_race == 4:
        enemy = Enemy(enemy_image, 50, 95, 630, rand_y, rand_speed)
    collision = sprite.spritecollideany(enemy, enemys)


    if not collision:
        enemys.add(enemy)

def animation_bg():
    global bg_y1, bg_y2, bg_speed, start_time, rand_interval, random_car
    #Тут ми робимо анімацію руху дороги
    if bg_y1 > 600:
        bg_y1 = -600

    if bg_y2 > 600:
        bg_y2 = -600
    window.blit(bg, (0, bg_y1))

    bg_y1 += bg_speed
    window.blit(bg, (0, bg_y2))
    bg_y2 += bg_speed

def animation_play():
    global e, keys, button_play, screen, while_game, button_exit, button_setting
    #Тут ми аніміруємо кнопку play
    button_play.draw()

    for e in event.get():
        keys = key.get_pressed()

        if e.type == MOUSEMOTION:
            mouse_x, mouse_y = e.pos#Получаємо позицію кліку
            if button_play.rect.collidepoint(mouse_x, mouse_y):#Якшо ми навели на кнопку ми міняємо зображення

                button_play.image = button_image_play_anim
            else:
                button_play.image = button_image_play
        if e.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = e.pos
            #Тут ми робимо дію кнопок
            if button_play.rect.collidepoint(mouse_x, mouse_y):
                screen = 'game'
                button_play.image = button_image_play

            if button_exit.rect.collidepoint(mouse_x, mouse_y):
                 while_game = False
            if button_setting.rect.collidepoint(mouse_x,mouse_y):
                screen = 'setting'


def animation_exit():
    global e, keys, screen, while_game, button_exit
    #Анімація виходу з ігри
    button_exit.draw()

    for e in event.get():
        keys = key.get_pressed()

        if e.type == MOUSEMOTION:
            mouse_x, mouse_y = e.pos
            if button_exit.rect.collidepoint(mouse_x, mouse_y):

                button_exit.image = button_image_exit_anim
            else:
                button_exit.image = button_image_exit

def random_booster():
    #Тут ми створюємо буст для ігрока
    rand_speeded = randint(3, 5)
    rand_race = randint(1, 4)
    rand_y = randint(600, 800)

    if rand_race == 1:
        boost = Enemy(bost_image, 50, 60, 210, rand_y, rand_speeded)
        bostery.add(boost)
    if rand_race == 2:
        boost = Enemy(bost_image, 50, 60, 350, rand_y, rand_speeded)
        bostery.add(boost)
    if rand_race == 3:
        boost = Enemy(bost_image, 50, 60, 500, rand_y, rand_speeded)
        bostery.add(boost)
    if rand_race == 4:
        boost = Enemy(bost_image, 50, 60, 630, rand_y, rand_speeded)
        bostery.add(boost)

#Тут ми створюємо групи ворогів і бустів
enemys = sprite.Group()
bostery = sprite.Group()

#Це наш ігрок
player = Player(player_image, 48, 80, 340, 300, 4.5)
#Тут сробили кнопки
button_again = Button(button_image_again, 200, 200, 350, 180, 1)
button_play = Button(button_image_play, 300, 200, 300, 20, 1)
button_exit = Button(button_image_exit, 250, 150, 330, 450, 1)
button_home = Button(button_image_home, 102, 102, 400, 400, 1)
button_setting = Button(button_image_setting, 100, 100, 0, 500, 1)

pause = Button(pause_image, 108, 108, 395, 220, 1)
#Створили вікно
window = display.set_mode((WIDTH, HEIGHT))

screen = 'menu'#Сцена яку потім ми міняємо
while_game = True
finish = False

FPS = 60
#Тут стровили текст
font1 = font.SysFont("Aril", 35)
font2 = font.SysFont("Aril", 100)
txt_lose_game = font2.render("You lose", True, (255, 0, 0))
txt_setting = font1.render('Tutorial:', True, (255, 255, 200))
txt_tutorial_setting = font1.render('Go up - w, down - s, Left - a, Right - d, SPACE - blim blim', True, (255, 255, 215))

#Тут ми получаємо час
clock = time.Clock()
start_time = time.get_ticks()
start_time_bost = time.get_ticks()
rand_interval = randint(500, 1500)
rand_interval_bost = randint(3000, 10000)
clock_time = 0
frames = 0

bg_y1 = 0
bg_y2 = -600
bg_speed = 3
while while_game:
    #Основний цикл

    with open('Record.txt', 'r') as f:
        record_time = int(f.readline())#Обновляємо рекорд
    if screen == 'menu':
        #Тут оформляємо меню

        animation_bg()

        animation_play()
        animation_exit()
        button_setting.draw()

        button_home.rect.y = 400
        button_home.rect.x = 400

        for e in event.get():
            keys = key.get_pressed()


    elif screen == 'setting':
        #Оформляємо налаштування
        animation_bg()
        window.blit(txt_tutorial_setting, (0, 50))

        window.blit(txt_setting, (0, 20))
        for e in event.get():

            keys = key.get_pressed()
            if e.type == QUIT:

                while_game = False
            if e.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = e.pos
                if button_home.rect.collidepoint(mouse_x, mouse_y):
                    clock_time = 0
                    screen = 'menu'
                    enemys.empty()
                    player.rect.x = 340
                    player.rect.y = 300
        button_home.rect.y = 490
        button_home.rect.x = 0
        button_home.draw()


    if finish == False and screen == 'game':

        animation_bg()

        for e in event.get():
            keys = key.get_pressed()
            if e.type == QUIT:
                while_game = False

            if e.type == KEYDOWN:#Якшо натиснули на спайс відіграли звук
                if e.key == K_SPACE:
                    bop_sound.play()

                if e.key == K_ESCAPE:

                    finish = True


                    pause.draw()
                    animation_play()
                    button_home.draw()
                    if e.type == MOUSEBUTTONDOWN:
                        if button_home.rect.collidepoint(mouse_x, mouse_y):
                            clock_time = 0
                            screen = 'menu'
                            enemys.empty()
                            player.rect.x = 340
                            player.rect.y = 300

        if time.get_ticks() - start_time_bost > rand_interval_bost:
            #Якшо настав час певний ми спавнемо буст
            random_booster()
            start_time_bost = time.get_ticks()
        if time.get_ticks() - start_time > rand_interval:
            # Якшо настав час певний ми спавнемо Ворога
            random_car()
            start_time = time.get_ticks()
        frames += 1
        if frames >= 55:
            clock_time += 1
            frames = 0



        spritelist = sprite.spritecollide(player, enemys, False)
        spritelist_bost = sprite.spritecollide(player, bostery, True)

        for collide in spritelist:
            #Якшо ми стукнулись з ворогом
            button_again.draw()
            if clock_time > record_time:
                record_time = clock_time

                with open('Record.txt', 'w') as f:
                    f.write(str(record_time))

            window.blit(txt_lose_game, (320, 100))

            button_home.draw()
            finish = True
        for collide in spritelist_bost:
            # Якшо ми підібрали буст
            player.speed += 0.3
            print(player.speed)
            bostery.empty()

        #Вимальовуємо текст екран ворогів і тд
        txt_time = font1.render(f"Time: {clock_time}", True, (200, 200, 100))
        txt_record_time = font1.render(f"Record time: {record_time}", True, (200, 200, 100))
        window.blit(txt_time, (0, 30))
        window.blit(txt_record_time, (0,60))
        player.draw()
        bostery.draw(window)
        enemys.draw(window)
        enemys.update()
        bostery.update()
        player.update()
    elif finish == True:
        #Якшо ми програли або поставили паузу
        for e in event.get():

            keys = key.get_pressed()
            if e.type == QUIT:
                while_game = False

            if e.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = e.pos

                if button_play.rect.collidepoint(mouse_x, mouse_y):
                    finish = False

                if button_again.rect.collidepoint(mouse_x, mouse_y):

                    clock_time = 0
                    enemys.empty()
                    bostery.empty()

                    player.rect.x = 340
                    player.rect.y = 300

                    finish = False
                elif button_home.rect.collidepoint(mouse_x, mouse_y):
                    clock_time = 0
                    screen = 'menu'
                    enemys.empty()
                    bostery.empty()
                    player.rect.x = 340
                    player.rect.y = 300
                    finish = False

    display.update()
    # Обмеження кадрів в секунду (FPS)
    clock.tick(FPS)
