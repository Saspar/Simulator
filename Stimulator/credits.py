import pygame
from constants import *


def init(pause):
    creditsound = pygame.mixer.music.load("creditsound.wav")
    pygame.mixer.music.play(1)

    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    pygame.mouse.set_visible(True)


def draw(screen):
    y = 0
    font_tnr = pygame.font.Font(None, 36)
    text = ["ALL IS FAKE"]
    for i in range (200): #4200-origin
        # fills screen with white, takes location from the middle of the screen, adds y and does it for 400 times
        screen.fill((255, 255, 255))
        for j in range(len(text)):
            text_back = font_tnr.render(text[j], 1, (255, 0, 0))
            textpos_back = text_back.get_rect()
            textpos_back.centerx = screen.get_rect().centerx
            textpos_back.centery = screen.get_rect().centery + 300 - y/3 + j * 50
            screen.blit(text_back, textpos_back)
        pygame.display.flip()
        y += 20 #1-origin
        pygame.time.delay(5)

    raise State_switcher('menu')


def on_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            raise State_switcher('menu')


def update():
    pass
