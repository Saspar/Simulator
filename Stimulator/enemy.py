import pygame
from character import Character
from constants import *

class Enemy(Character):

    def __init__(self, x, y, enemy_icon):
        self.x = x
        self.y = y
        self.x_speed = 1
        self.y_speed = 1
        self.icon = enemy_icon
        self.dead = False
        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])
        self.dead = False

    def draw(self, screen, cam_pos):
        if not self.dead:
            screen.blit(self.icon, [self.x - cam_pos[0], self.y - cam_pos[1]])

    def update(self, player, map_data):
        if not self.dead:
            tile_x = (self.x // TILESIZE) + 1
            tile_y = (self.y // TILESIZE) + 1

            # left = 1, up = 2, right = 3, down = 4
            possible_dirs = []

            # print(map_data)

            try:
                if map_data[tile_y][tile_x-1] == 0:
                    possible_dirs.append(1)
            except:
                pass

            try:
                if map_data[tile_y-1][tile_x] == 0:
                    possible_dirs.append(2)
            except:
                pass

            try:
                if map_data[tile_y][tile_x+1] == 0:
                    possible_dirs.append(3)
            except:
                pass

            try:
                if map_data[tile_y+1][tile_x] == 0:
                    possible_dirs.append(4)
            except:
                pass

            if self.x > player.x and 1 in possible_dirs:
                self.x -= self.x_speed

            if self.x < player.x and 3 in possible_dirs:
                self.x += self.x_speed
            # Movement along y direction
            if self.y < player.y and 4 in possible_dirs:
                self.y += self.y_speed
            elif self.y > player.y and 2 in possible_dirs:
                self.y -= self.y_speed

            self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])

    def collide(self, bullet_list):
        if not self.dead:
            for i in bullet_list:
                if self.rect.collidepoint(i.pos):
                    print("Kera has dieded, U mordoror!")
                    self.dead = True