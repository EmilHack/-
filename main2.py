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



#призрак
ghost = pygame.image.load('images/ghost (2).png').convert_alpha()
ghost_in_game = []
ghost_timer = pygame.USEREVENT + 2
pygame.time.set_timer(ghost_timer, 1000)

kitty = pygame.image.load('images/kitty.png').convert_alpha()
kitty_in_game = []
kitty_timer = pygame.USEREVENT + 3
pygame.time.set_timer(kitty_timer, 1200)



bg_sound.play()
#спрайты
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

bg_x2 = bg_x+900




gameplay = True

running = True
# while True: # цикл, чтобы экран был включен
#
# if gameplay:
# screen.blit(bg, (bg_x, -100))
# screen.blit(bg, (bg_x2, -100))
# # Смена фона
# if bg_x == -900:
# bg_x = 0
# if bg_x2 == -1800:
# bg_x2 = 900
# if len(ghost_in_game) == 10:
# ghost_in_game.clear()
#
#
# player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))
#
# if ghost_in_game:
# for (i, el) in enumerate(ghost_in_game):
# screen.blit(ghost, el)
# el.x -= 10
#
# if el.x < -10:
# ghost_in_game.pop(i)
#
#
# if player_rect.colliderect(el):
# gameplay = False
# if kitty_in_game:
# for (i, el) in enumerate(kitty_in_game):
# screen.blit(kitty, el)
# el.x -= 10
#
# if el.x < -10:
# kitty_in_game.pop(i)
#
#
# if player_rect.colliderect(el):
# gameplay = False
#
#
#
#
#
#
# keys = pygame.key.get_pressed()
# if keys[pygame.K_LEFT] and player_x > 50: # передвижение персонажа
# player_x -= player_speed
# elif keys[pygame.K_RIGHT] and player_x < 850:
# player_x += player_speed
#
# # прыжок
# if not is_jump:
# if keys[pygame.K_SPACE]:
# is_jump = True
# else:
# if jump_count >= -7:
# if jump_count > 0:
# player_y -= (jump_count ** 2) / 2
# else:
# player_y += (jump_count ** 2) / 2
# jump_count -= 1
# else:
# is_jump = False
# jump_count = 7
#
#
# if keys[pygame.K_LEFT]: #смена анимации
# screen.blit(walk_left[player_anim_count], (player_x, player_y))
# else:
# screen.blit(walk_right[player_anim_count], (player_x, player_y))
#
#
#
# if player_anim_count == 5: # переключение анимации
# player_anim_count = 0
# else:
# player_anim_count += 1
# bg_x -=2
# bg_x2 -=2
# else:
# screen.fill((0,0,0))
# screen.blit(lose_label,  (300, 200))
# screen.blit(restart_label, restart_label_rect)
# bg_sound.stop()
#
# mouse = pygame.mouse.get_pos()
# if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
# gameplay = True
# bg_sound.play()
# player_x = 60
# ghost_in_game.clear()
# kitty_in_game.clear()
# bg_x = 0
# bg_x2 = bg_x + 900
# pygame.display.update() # обновление экрана
# for event in pygame.event.get(): # завершение цикла и выход из приложения
# if event.type == pygame.QUIT:
# running = False
# pygame.quit()
# if event.type == ghost_timer:
# ghost_in_game.append(ghost.get_rect(topleft=(920, 500)))
# if event.type == kitty_timer:
# kitty_in_game.append(kitty.get_rect(topleft=(920, 400)))
# #скорость игры
# clock.tick(30)

# Initialize Pygame, load images, sounds, etc.
# ...

def draw_background():
    screen.blit(bg, (bg_x, -100))
    screen.blit(bg, (bg_x2, -100))

def update_background():
    global bg_x, bg_x2
    if bg_x == -900:
        bg_x = 0
    if bg_x2 == -1800:
        bg_x2 = 900
    bg_x -= 2
    bg_x2 -= 2
keys = pygame.key.get_pressed()
def draw_player():
    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

def update_player():
    global player_x, player_y, is_jump, jump_count, player_anim_count
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 850:
        player_x += player_speed
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
    if player_anim_count == 5:
        player_anim_count = 0
    else:
        player_anim_count += 1


def draw_ghosts():
    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    global ghost_in_game
    for (i, el) in enumerate(ghost_in_game):
        screen.blit(ghost, el)
        el.x -= 10
        if el.x < -10:
            ghost_in_game.pop(i)
        if player_rect.colliderect(el):
            gameplay = False

def draw_kitties():
    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    global kitty_in_game
    for (i, el) in enumerate(kitty_in_game):
        screen.blit(kitty, el)
        el.x -= 10
        if el.x < -10:
            kitty_in_game.pop(i)
        if player_rect.colliderect(el):
            gameplay = False

def handle_events():
    global running, gameplay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ghost_timer:
            ghost_in_game.append(ghost.get_rect(topleft=(920, 500)))
        if event.type == kitty_timer:
            kitty_in_game.append(kitty.get_rect(topleft=(920, 400)))

def draw_game_over_screen():
    screen.fill((0,0,0))
    screen.blit(lose_label,  (300, 200))
    screen.blit(restart_label, restart_label_rect)
    bg_sound.stop()
    mouse = pygame.mouse.get_pos()
    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay = True
        bg_sound.play()
        player_x = 60
        ghost_in_game.clear()
        kitty_in_game.clear()
        bg_x = 0
        bg_x2 = bg_x + 900

# Game loop
while True:
    if gameplay:
        draw_background()
        update_background()
        draw_player()
        update_player()
        draw_ghosts()
        draw_kitties()
    else:
        draw_game_over_screen()
    pygame.display.update()
    handle_events()
    clock.tick(30)

