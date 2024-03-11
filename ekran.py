import pygame

screen = pygame.display.set_mode((900,600), pygame.RESIZABLE)
bgover = pygame.image.load('images/image.psd(10).png').convert_alpha()
score = 0
scores = 0


def over(restart_label, restart_label_rect):
    global bgO_x1, bgO_x2, scores, score
    bgO_x1 = 0
    bgO_x2 = 900
    screen.blit(bgover, (bgO_x1, 0))
    screen.blit(bgover, (bgO_x2, -100))
    screen.blit(restart_label, restart_label_rect)
    scores = 0
    score = 0

score_all = 1

def draw_background(bg, bg_x, bg_x2, label):
    global score, scores, score_all
    screen.blit(bg, (bg_x, -100))
    screen.blit(bg, (bg_x2, -100))

    if scores == 30:
        score += score_all
        scores = 0
        score_all += 1
    else:
        scores += 1
    screen.blit(label.render(str(score), False, (0,0,0)), (500, 300))


def setdisplay():
    icon = pygame.image.load('images/icon.png').convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption("КАЗИНО ОНЛАЙН")