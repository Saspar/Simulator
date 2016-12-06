import pygame
from constants import *

fade = 0
fadeIn = True
musicneed = True

def init(pause):
    global intropic
    intropic = pygame.image.load("intropic.png").convert()
    introsound = pygame.mixer.music.load("introsound.wav")
    pygame.mouse.set_visible(False)
    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


def on_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
            pygame.mixer.music.stop()
            raise State_switcher('menu')


def update():
    pass


def draw(screen):
    global fade
    global fadeIn
    global intropic, musicneed
    global screen_w, screen_h
    if fadeIn:
        fade += 2.5
    else:
        fade -= 2.5

    screen.fill((255, 255, 255))
    intropic.set_alpha(fade)
    screen.blit(intropic, (0,0))

    if musicneed:
        pygame.mixer.music.play()
        musicneed = False

    if fade == 255:
        fadeIn = False

    elif fade == 0 and not fadeIn:
        pygame.mixer.music.stop()
        raise State_switcher('menu')
