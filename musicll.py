import pygame
import random
music_player = False
tracks = [
    'sound/mia.mp3',
    'sound/m0meNteR - Metamorphosed Freddy Fazbear_(Muz-Monster.ru).mp3',
    'sound/Icyk_Cyper_feat_Igor_cyba_-_Dymok_76563985.mp3',
    'sound/gedagedago (128kbps).mp3']

def random_track():
    global random_number
    # Генерация случайного числа от 0 до 3
    random_number = random.randint(0, 3)
def treck1():
    global music_player, tracks
    random_track()
    if not music_player:
         pygame.mixer.music.load(tracks[random_number])
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