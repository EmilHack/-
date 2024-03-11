import pygame
from pygame import mixer
from musicll import treck1, treck2
from ekran import over, draw_background, setdisplay
from движение import kittyjimp, runkitty, animends
pygame.init()
mixer.init()
screen = pygame.display.set_mode((900, 600), pygame.RESIZABLE)
setdisplay()
bg = pygame.image.load('images/bg.jpg').convert_alpha()
label = pygame.font.SysFont(str(None), 50)
restart_label = label.render('ИГРАТЬ', False, (14, 200, 255))
restart_label_rect = restart_label.get_rect(topleft=(270, 300))
meter = 0
jump_ukr = 1
jump_check = False
def update_background():
    global bg_x, bg_x2
    if bg_x == -900:
        bg_x = 0
    if bg_x2 == 0:
        bg_x2 = 900
    bg_x -= 2
    bg_x2 -= 2
def dead():
    global gameplay, meter, jump_check, jump_ukr, el_count
    player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))
    if ghost_in_game:
        for (i, el) in enumerate(ghost_in_game):
            screen.blit(ghost, el)
            el.x -= 10
            el_count = el.y
            if meter == 90:
                jump_check = True
            else:
                meter += 1
            if jump_check:
                if jump_ukr < 14:
                    el.y -= 1
                    el.x -= 10
                    jump_ukr += 1
                else:
                    el.y = el_count
                    jump_ukr = 1
                    el.x += 30
                    jump_check = False
                    meter = 0
            if el.x < -5:
                ghost_in_game.pop(i)
            if player_rect.colliderect(el):
                gameplay = False
def restartik():
    global gameplay, player_x, bg_x2, bg_x
    mouse = pygame.mouse.get_pos()
    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay = True
        player_x = 60
        ghost_in_game.clear()
        bg_x = 0
        bg_x2 = bg_x + 900
def walk():
    global walk_left, walk_right
    walk_left = [
        pygame.image.load('images/sprite_left/s1.png').convert_alpha(),
        pygame.image.load('images/sprite_left/s2.png').convert_alpha(),
        pygame.image.load('images/sprite_left/s3.png').convert_alpha(),
        pygame.image.load('images/sprite_left/s4.png').convert_alpha(),
        pygame.image.load('images/sprite_left/s5.png').convert_alpha(),
        pygame.image.load('images/sprite_left/s6.png').convert_alpha()]
    walk_right = [
        pygame.image.load('images/sprite_right/s1.png').convert_alpha(),
        pygame.image.load('images/sprite_right/s2.png').convert_alpha(),
        pygame.image.load('images/sprite_right/s3.png').convert_alpha(),
        pygame.image.load('images/sprite_right/s4.png').convert_alpha(),
        pygame.image.load('images/sprite_right/s5.png').convert_alpha(),
        pygame.image.load('images/sprite_right/s6.png').convert_alpha()]
def iventik():
    global running, mouse, score, gameplay
    pygame.display.update()  # обновление экрана
    for event in pygame.event.get():  # завершение цикла и выход из приложения
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_in_game.append(ghost.get_rect(topleft=(900, 500)))
    clock = pygame.time.Clock()
    clock.tick(30)
ghost = pygame.image.load('images/ukr.png').convert_alpha()
ghost_in_game = []
ghost_timer = pygame.USEREVENT + 2
pygame.time.set_timer(ghost_timer, 1000)
bg_x = 0
player_x = 60
player_y = 500
player_speed = 5
jump_count = 7
bg_x2 = 900
gameplay = False
running = True
while True:
    if gameplay:
        treck1()
        walk()
        draw_background(bg, bg_x, bg_x2,label)
        update_background()
        dead()
        player_x, player_speed = runkitty(player_speed, player_x)
        player_y, jump_count = kittyjimp(player_y, jump_count)
        animends(screen, walk_left, walk_right, player_x, player_y, bg_x, bg_x2)
    else:
        over(restart_label, restart_label_rect)
        treck2()
        restartik()
        score = 0
        scores = 0
    iventik()