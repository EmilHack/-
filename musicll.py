import pygame
import random
music_player = False
tracks = [
    'sound/mia.mp3',
    'sound/m0meNteR - Metamorphosed Freddy Fazbear_(Muz-Monster.ru).mp3',
    'sound/Icyk_Cyper_feat_Igor_cyba_-_Dymok_76563985.mp3',
    'sound/gedagedago (128kbps).mp3',
    'sound/Tom_Cat_-_Chin_Cheng_hanji_75546186.mp3']


def random_track():
    global random_number
    random_number = random.randint(0, 4)


def treck1():
    global music_player, tracks
    random_track()
    if not music_player:
         pygame.mixer.music.load(tracks[random_number])
         pygame.mixer.music.play()
         music_player = True
    if not pygame.mixer.music.get_busy():
         music_player = False


def random_track_over():
    global random_number2
    random_number2 = random.randint(0, 6)


bg_soundEND = [
    'sound/over/NVP.mp3',
    'sound/over/nvp2.mp3',
    'sound/over/Akira_Yamaoka_Silent_Hill_3_OST_14_Never_Forgive_Me_Never_Forget.mp3',
    'sound/over/C418_-_Haggstrom_30921643.mp3',
    'sound/over/C418_-_Minecraft_30921694.mp3',
    'sound/over/C418_-_Subwoofer_Lullaby_30921632.mp3',
    'sound/over/KXBRIGU - AFRAID_ Buckshot Roulette Phonk.mp3'
]





def treck2():
    global music_player, bg_soundEND
    random_track_over()
    if music_player:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(bg_soundEND[random_number2])
        pygame.mixer.music.play()
        music_player = False
    if not pygame.mixer.music.get_busy():
        music_player = True