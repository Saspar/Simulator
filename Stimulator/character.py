import pygame
from constants import *

character_icon = pygame.image.load("player_boy.png")

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, character_icon):
        pass

    def update(self, rect_list):
        pass

    def draw(self, screen, cam_pos):
        pass