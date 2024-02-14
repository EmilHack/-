import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((900,500)) #, flags=pygame.NOFRAME
# flags=pygame.NOFRAME убирает верхнии кнопки
screen.fill((255, 0, 179))
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
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 1000)


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
player_y = 430

is_jump = False
jump_count = 7

bg_x2 = bg_x+900


gameplay = True

running = True
while True: # цикл, чтобы экран был включен


    if gameplay:
        screen.blit(bg, (bg_x, -100))
        screen.blit(bg, (bg_x2, -100))




        player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))

        if ghost_in_game:
            for (i, el) in enumerate(ghost_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_in_game.pop(i)


                if player_rect.colliderect(el):
                    gameplay = False






        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 50: # передвижение персонажа
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 850:
            player_x += player_speed

    # прыжок
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


        if keys[pygame.K_LEFT]: #смена анимации
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))



        if player_anim_count == 5: # переключение анимации
            player_anim_count = 0
        else:
            player_anim_count += 1
        bg_x -=2

        if bg_x == 900: # обновление фона
            bg_x = 0
    else:
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





    pygame.display.update() # обновление экрана
    for event in pygame.event.get(): # завершение цикла и выход из приложения
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_in_game.append(ghost.get_rect(topleft=(920, 425 )))



#скорость игры
    clock.tick(20)



