import pygame
screen = pygame.display.set_mode((900,600), pygame.RESIZABLE)
bgover = pygame.image.load('images/image.psd(10).png').convert_alpha()


def over():
    global bgO_x1, bgO_x2
    bgO_x1 = 0
    bgO_x2 = 900
    screen.blit(bgover, (bgO_x1, 0))
    screen.blit(bgover, (bgO_x2, -100))


def draw_background(bg, bg_x, bg_x2):
    screen.blit(bg, (bg_x, -100))
    screen.blit(bg, (bg_x2, -100))


def setdisplay():
    icon = pygame.image.load('images/icon.png').convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption("КАЗИНО ОНЛАЙН")