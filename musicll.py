import pygame
music_player = False


def treck1():
    global music_player
    if not music_player:
         bg_sound = 'sound/gedagedago (128kbps).mp3'
         pygame.mixer.music.load(bg_sound)
         pygame.mixer.music.play()
         music_player = True
    if not pygame.mixer.music.get_busy():
         music_player = False


def treck2():
    global music_player
    if music_player:
        pygame.mixer.music.stop()
        bg_soundEND = 'sound/NVP.mp3'
        pygame.mixer.music.load(bg_soundEND)
        pygame.mixer.music.play()
        music_player = False
    if not pygame.mixer.music.get_busy():
        music_player = True