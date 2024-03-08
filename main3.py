import pygame
pygame.init()


clock = pygame.time.Clock()

screen = pygame.display.set_mode((900,600), pygame.RESIZABLE) #, flags=pygame.NOFRAME
# flags=pygame.NOFRAME убирает верхнии кнопки

pygame.display.set_caption("КАЗИНО ОНЛАЙН")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)



label = pygame.font.Font('font/RubikGlitchPop-Regular.ttf', 50)
lose_label = label.render('ПОРАЖЕНИЕ', False, (255, 255, 255))
restart_label = label.render('ИГРАТЬ СНОВА', False, (14, 200, 255))
restart_label_rect = restart_label.get_rect(topleft=(270, 300))
bg = pygame.image.load('images/bg.jpg').convert_alpha()


bg_sound = pygame.mixer.Sound('sound/mia.mp3')

''' функции '''
def draw_background():
    screen.blit(bg, (bg_x, -100))
    screen.blit(bg, (bg_x2, -100))
def update_background():
    global bg_x, bg_x2
    if bg_x == -900:
        bg_x = 0
    if bg_x2 == 0:
        bg_x2 = 900
    bg_x -= 2
    bg_x2 -= 2
def dead():
    global gameplay #баг3
    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    if ghost_in_game:
        for (i, el) in enumerate(ghost_in_game):
            screen.blit(ghost, el)
            el.x -= 10
            if el.x < -5:
                ghost_in_game.pop(i)
            if player_rect.colliderect(el):
                gameplay = False
def runkitty():
    global player_x
    if keys[pygame.K_LEFT] and player_x > 50:  # передвижение персонажа
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 850:
        player_x += player_speed
def kittyjimp():
    global is_jump, jump_count, player_y
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7
def animends():
    global player_anim_count, bg_x, bg_x2
    if keys[pygame.K_LEFT]:  # смена анимации
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if player_anim_count == 5:  # переключение анимации
        player_anim_count = 0
    else:
        player_anim_count += 1
    bg_x -= 2
    bg_x2 -= 2
def restartik():
    global gameplay, player_x, bg_x2, bg_x
    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay = True
        bg_sound.play()
        player_x = 60
        ghost_in_game.clear()
        bg_x = 0
        bg_x2 = bg_x + 900
''' запуск и -запуск'''
def iventik():
    global running
    pygame.display.update()  # обновление экрана
    for event in pygame.event.get():  # завершение цикла и выход из приложения
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_in_game.append(ghost.get_rect(topleft=(900, 500)))


ghost = pygame.image.load('images/ghost (2).png').convert_alpha()
ghost_in_game = []
ghost_timer = pygame.USEREVENT + 2
pygame.time.set_timer(ghost_timer, 1000)


bg_sound.play()
#спрайты
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

player_anim_count = 0
bg_x = 0

#5
player_speed = 5
player_x = 60
player_y = 500
is_jump = False
jump_count = 7

bg_x2 = 900


gameplay = True

running = True
while True: # цикл, чтобы экран был включен


    if gameplay:
        walk()
        draw_background()
        update_background()
        dead()
        keys = pygame.key.get_pressed()
        runkitty()
        kittyjimp()
        animends()
    else:
        screen.fill((0,0,0))
        screen.blit(lose_label,  (300, 200))
        screen.blit(restart_label, restart_label_rect)
        bg_sound.stop()
        mouse = pygame.mouse.get_pos()
        restartik()
    iventik()
#скорость игры
    clock.tick(30)



