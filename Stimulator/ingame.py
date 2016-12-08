import player
from constants import *
import pygame
import map
import enemy
import pie
from bullet import *

cam_position = [0, 0]
bullet_list = []

def init(pause):
    global player_obj, player_icon, enemy_icon, enemy_obj, bullet_obj, pie1_obj, pie2_obj, pie3_obj, score

    enemy_icon = pygame.image.load("Kera.png")
    pie_icon = pygame.image.load("Pie.png")

    #PLAYER
    player_obj = player.Player(100, 150)

    #ENEMY
    enemy_obj = enemy.Enemy(300, 250, enemy_icon)

    #OBJECTS
    pie1_obj = pie.Pie1(100, 250, pie_icon)
    pie2_obj = pie.Pie1(1250, 200, pie_icon)
    pie3_obj = pie.Pie1(100, 300, pie_icon)

    gamemusic = pygame.mixer.music.load("gamesound.wav")
    pygame.mixer.music.play(-1)

    #Mute/unmute
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
    #food1_obj.update(player_obj, map.map1_data)
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

    enemy_obj.collide(bullet_list)
    pie1_obj.collide(bullet_list)
    pie2_obj.collide(bullet_list)
    pie3_obj.collide(bullet_list)

def draw(screen):
    screen.fill((0, 200, 0)) #suvi

    map.draw(screen, cam_position)
    enemy_obj.draw(screen, cam_position)
    pie1_obj.draw(screen, cam_position)
    pie2_obj.draw(screen, cam_position)
    pie3_obj.draw(screen, cam_position)
    player_obj.draw(screen, cam_position)

    for i in bullet_list:
        i.draw(screen, cam_position)