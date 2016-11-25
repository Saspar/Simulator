# game has been made by Gert Jõgiste,  Karl Caspar Sünter, Rauno Jaaska, Allan Alikas, Andre Viibur
# aka Arvutiklubi's progelaagri team 1 in NRG 12/13.11.2016
import pygame
import sys
from constants import *
from pygame.locals import *

current_state = ''

pause = False

def quit_game():
    pygame.quit()
    sys.exit()


def switch_state(new_state):
    global current_state, pause

    current_state = __import__(new_state)
    current_state.init(pause)

if __name__ == '__main__':

    pygame.init()

    flags = pygame.SRCALPHA | pygame.DOUBLEBUF

    screen = pygame.display.set_mode((screen_w, screen_h), flags)
    clock = pygame.time.Clock()
    ms = clock.tick(fps)

    pause = False

    switch_state('intro')

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                else:
                    current_state.on_event(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if not pause:
                            pygame.mixer.music.pause()
                            pause = True
                        else:
                            pygame.mixer.music.unpause()
                            pause = False

            current_state.update()
            current_state.draw(screen)

            pygame.display.flip()

            ms = clock.tick(fps)
        except State_switcher as e:
            switch_state(e.value)
