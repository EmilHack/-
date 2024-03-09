import pygame
screen = pygame.display.set_mode((900,600), pygame.RESIZABLE)
bgover = pygame.image.load('images/image.psd(10).png').convert_alpha()
def over():
    global bgO_x1, bgO_x2
    bgO_x1 = 0
    bgO_x2 = 900
    screen.blit(bgover, (bgO_x1, 0))
    screen.blit(bgover, (bgO_x2, -100))