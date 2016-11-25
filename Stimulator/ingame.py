import player
from constants import *
import pygame
import map
import enemy
from bullet import *

cam_position = [0, 0]
bullet_list = []


def init(pause):
    global player_obj, player_icon, enemy_icon, enemy_obj, bullet_obj
    enemy_icon = pygame.image.load("Kera.png")
    #player_icon = pygame.image.load("player.png")
    player_obj = player.Player(100, 650)
    enemy_obj = enemy.Enemy(300, 1800, enemy_icon)

    gamemusic = pygame.mixer.music.load("gamesound.wav")
    pygame.mixer.music.play(-1)

    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    pygame.mouse.set_visible(True)


def on_event(event):
    player_obj.on_event(event, bullet_list)


def update():
    player_obj.update(map.get_rect_list())
    enemy_obj.update(player_obj, map.map1_data)
    cam_position[0] = player_obj.x - screen_w/2 + player_obj.rect.w/2
    cam_position[1] = player_obj.y - screen_h/2 + player_obj.rect.h/2

    for i in bullet_list:
        i.update(map.map1_data)

    dead_list = []

    for i, bullet in enumerate(bullet_list):
        if bullet.dead == True:
            dead_list.append(i)

    for i in sorted(dead_list)[::-1]:

        bullet_list.pop(i)
    # print(cam_position, player_obj.x, player_obj.y)

    enemy_obj.collide(bullet_list)


def draw(screen):
    screen.fill((255, 255, 255)) #talv ju!

    map.draw(screen, cam_position)
    enemy_obj.draw(screen, cam_position)
    player_obj.draw(screen, cam_position)

    for i in bullet_list:
        i.draw(screen, cam_position)