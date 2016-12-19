import pygame
from character import Character
from constants import *

class Enemy(Character):

    def __init__(self, x, y, enemy_icon):
        self.x = x
        self.y = y
        self.x_speed = keraspeed[0]
        self.y_speed = keraspeed[0]
        self.x_speed1 = keraspeed[0]
        self.y_speed1 = keraspeed[0]
        self.icon = enemy_icon
        self.dead = False
        self.angry = False
        self.timer = keratimer[0]
        self.angryspeed = keraspeed2[0]
        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])

    def draw(self, screen, cam_pos):
        if not self.dead:
            screen.blit(self.icon, [self.x - cam_pos[0], self.y - cam_pos[1]])

    def update(self, player, map_data):
        if not self.dead:
            tile_x = (self.x + 40) // (TILESIZE + 3 ) + 1
            tile_y = self.y // TILESIZE + 1

            if self.x_speed == (self.x_speed1 + self.angryspeed) and self.timer > 0:
                self.timer -= 1
                if self.timer == 0 and self.x_speed == self.x_speed1 + self.angryspeed:
                    self.x_speed -= keraspeed2[0]
                    self.y_speed -= keraspeed2[0]
                    self.timer = keratimer[0]
                    self.angry = False
                    print ("Kyll ma sulle n2itan!")

            # left = 1, up = 2, right = 3, down = 4
            possible_dirs = []

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
            if self.y < player.y and 4 in possible_dirs:
                self.y += self.y_speed
            if self.y > player.y and 2 in possible_dirs:
                self.y -= self.y_speed

            self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])

    def collide(self, bullet_list):
        if not self.angry:
            for i in bullet_list:
                if self.rect.collidepoint(i.pos):
                    print("GRRRR!!!")
                    self.angry = True
                    self.x_speed += keraspeed2[0]
                    self.y_speed += keraspeed2[0]