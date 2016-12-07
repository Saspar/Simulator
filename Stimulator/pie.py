import pygame
from character import Character
from constants import *

class Pie1(Character):

    def __init__(self, x, y, food1_icon):
        self.x = x
        self.y = y
        self.icon = food1_icon
        self.dead = False
        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])

    def draw(self, screen, cam_pos):
        if not self.dead:
            screen.blit(self.icon, [self.x - cam_pos[0], self.y - cam_pos[1]])

    def collide(self, bullet_list):
        if not self.dead:
            for i in bullet_list:
                if self.rect.collidepoint(i.pos):
                    print("Nom-nom-nom...")
                    self.dead = True