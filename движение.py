import pygame

keys = pygame.key.get_pressed()

is_jump = False
player_anim_count = 0
def kittyjimp(player_y):
    global is_jump, jump_count
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


def runkitty(player_speed, player_x):
    if keys[pygame.K_LEFT] and player_x > 50:  # передвижение персонажа
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 850:
        player_x += player_speed


def animends(screen, walk_left, walk_right, player_x, player_y, bg_x, bg_x2):
    global player_anim_count
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


