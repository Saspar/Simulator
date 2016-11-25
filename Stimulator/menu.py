import pygame
from constants import *
import main


def init(pause):
    global options, select, buttonsound
    options = ["Play", "Credits", "Quit"]
    select = 0

    pygame.mixer.music.set_volume(0.5)
    menumusic = pygame.mixer.music.load("menusound.wav")
    pygame.mixer.music.play(-1)
    buttonsound = pygame.mixer.Sound("buttonsound.wav")
    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


def on_event(e):
    global options, select, buttonsound

    if e.type == pygame.KEYDOWN:

        if e.key == pygame.K_DOWN or e.key == pygame.K_s:
            pygame.mixer.Sound.play(buttonsound)
            if select + 1 == len(options):
                select = 0
            else:
                select += 1

        if e.key == pygame.K_UP or e.key == pygame.K_w:
            pygame.mixer.Sound.play(buttonsound)
            if select == 0:
                select = len(options) - 1
            else:
                select -= 1

        if e.key == pygame.K_RETURN or e.key == pygame.K_SPACE:
            if select == 0:
                raise State_switcher('ingame')
            if select == 1:
                raise State_switcher('credits')
            if select == 2:
                main.quit_game()


def update():
    pass


def draw(screen):
    screen.fill((0, 255, 0))
    font_tnr = pygame.font.SysFont(size=36, name="britannic")
    global select

    if select == 0:
        text_start = font_tnr.render("Start", 1, (255, 0, 0))
        textpos_start = text_start.get_rect()
        textpos_start.centerx = screen.get_rect().centerx
        textpos_start.centery = screen.get_rect().centery

    else:
        text_start = font_tnr.render("Start", 1, (10, 10, 10))
        textpos_start = text_start.get_rect()
        textpos_start.centerx = screen.get_rect().centerx
        textpos_start.centery = screen.get_rect().centery

    if select == 1:
        text_credits = font_tnr.render("Credits", 3, (255, 0, 0))
        textpos_credits = text_credits.get_rect()
        textpos_credits.centerx = screen.get_rect().centerx
        textpos_credits.centery = screen.get_rect().centery + 50
    else:
        text_credits = font_tnr.render("Credits", 3, (10, 10, 10))
        textpos_credits = text_credits.get_rect()
        textpos_credits.centerx = screen.get_rect().centerx
        textpos_credits.centery = screen.get_rect().centery + 50

    if select == 2:
        text_quit = font_tnr.render("Quit", 3, (255, 0, 0))
        textpos_quit = text_quit.get_rect()
        textpos_quit.centerx = screen.get_rect().centerx
        textpos_quit.centery = screen.get_rect().centery + 100
    else:
        text_quit = font_tnr.render("Quit", 3, (10, 10, 10))
        textpos_quit = text_quit.get_rect()
        textpos_quit.centerx = screen.get_rect().centerx
        textpos_quit.centery = screen.get_rect().centery + 100

    screen.blit(text_quit, textpos_quit)
    screen.blit(text_start, textpos_start)
    screen.blit(text_credits, textpos_credits)
