import pygame
from constants import *
from character import Character
from bullet import *
import math
LEFT = 1

class Player(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0

        self.angle = 0

        self.acc_x = 0
        self.acc_y = 0

        self.max_acc = 0.2
        self.max_speeed = 9

        self.w = False
        self.a = False
        self.s = False
        self.d = False

        self.last_y = None
        self.last_x = None

        self.icon = pygame.image.load("player_girl.png")

        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])

    def on_event(self, event, bullet_list):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            self.shoot(event.pos, bullet_list)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.acc_y = -self.max_acc
                # self.icon = (self.player_icon_up)
                if self.y_speed != 0:
                    self.y_speed = - self.y_speed
                self.w = True
                self.last_y = "w"

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.acc_x = -self.max_acc
                # self.icon = self.player_icon_left
                if self.x_speed != 0:
                    self.x_speed = - self.x_speed
                self.a = True
                self.last_x = "a"

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.acc_x = self.max_acc
                # self.icon = self.player_icon_right
                if self.x_speed != 0:
                    self.x_speed = -self.x_speed
                self.d = True
                self.last_x = "d"

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.acc_y = self.max_acc
                # self.icon = self.player_icon_down
                if self.y_speed != 0:
                    self.y_speed = -self.y_speed
                self.s = True
                self.last_y = "s"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.acc_y = - self.max_acc
                self.w = False

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.acc_y = self.max_acc
                self.s = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.acc_x = - self.max_acc
                self.a = False

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.acc_x = self.max_acc
                self.d = False


    def shoot(self, mouse_pos, bullet_list):
        h = math.sqrt((math.pow(-(screen_w/2 - mouse_pos[0]), 2)) +
                      (math.pow(-(screen_h / 2 - mouse_pos[1]), 2)))
        vel_x = (-(screen_w/2 - mouse_pos[0])) / h
        vel_y = (-(screen_h/2 - mouse_pos[1])) / h
        bullet_list.append(Bullet(self.x, self.y, vel_x, vel_y))

    def update(self, rect_list):

        if abs(self.x_speed) < self.max_speeed:
            self.x_speed += self.acc_x

        if abs(self.y_speed) < self.max_speeed:
            self.y_speed += self.acc_y

        if self.x_speed != 0:
            if not self.collide(rect_list, self.x_speed, 0):
                self.x += self.x_speed

        if self.y_speed != 0:
            if not self.collide(rect_list, 0, self.y_speed):
                self.y += self.y_speed


        if self.y_speed < 0 and not self.w:
            if not self.s:
                self.acc_y = 0
                self.y_speed = 0
            else:
                self.acc_y = self.max_acc
                self.y_speed = - self.y_speed

        if self.y_speed > 0 and not self.s:
            if not self.w:
                self.acc_y = 0
                self.y_speed = 0
            else:
                self.acc_y = - self.max_acc
                self.y_speed = -self.y_speed

        if self.x_speed > 0 and not self.d:
            if not self.a:
                self.acc_x = 0
                self.x_speed = 0
            else:
                self.acc_x = - self.max_acc
                self.x_speed = - self.x_speed

        if self.x_speed < 0 and not self.a:
            if not self.d:
                self.acc_x = 0
                self.x_speed = 0
            else:
                self.acc_x = self.max_acc
                self.x_speed = abs(self.x_speed)



        if self.last_y == "w" and self.w and not self.acc_y < 0:
            self.acc_y = - self.max_acc
            self.acc_y = self.acc_y
        if self.last_y == "s" and self.s and not self.acc_y > 0:
            self.acc_y = self.max_acc
            self.acc_y = self.acc_y
        if self.last_x == "a" and self. a and not self.acc_x < 0:
            self.acc_x = - self.max_acc
            self.acc_x = self.acc_x
        if self.last_x == "d" and self.d and not self.acc_x > 0:
            self.acc_x = self.max_acc
            self.acc_x -= self.acc_x

        self.rect.x = self.x
        self.rect.y = self.y

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = screen_w / 2 - mouse_pos[0]
        mouse_y = screen_h/2 - mouse_pos[1]
        mousa_x = abs(mouse_x)
        mousa_y = abs(mouse_y)

        if mouse_x > 0 > mouse_y:
            self.angle = math.atan(mousa_y/mousa_x) / (2 * math.pi) * 360
        elif mouse_x < 0 and mouse_y < 0:
            self.angle = 90 + math.atan(mousa_x/mousa_y) / (2 * math.pi) * 360
        elif mouse_x < 0 < mouse_y:
            self.angle = 180 + math.atan(mousa_y/mousa_x) / (2 * math.pi) * 360
        elif mouse_x > 0 and mouse_y > 0:
            self.angle = 270 + math.atan(mousa_x/mousa_y) / (2 * math.pi) * 360

    def draw(self, screen, cam_pos):
        surf = pygame.transform.rotate(self.icon, self.angle)
        saiz = surf.get_rect().size
        screen.blit(surf, [screen_w/2 - saiz[0]/2, screen_h/2 - saiz[1]/2])

    def collide(self, wall_list, dx, dy):
        rect = pygame.Rect([screen_w/2 - TILESIZE/2 + 5 + dx,
                            screen_h/2-TILESIZE/2 + 5 + dy, TILESIZE - 10, TILESIZE - 10])

        index = rect.collidelist(wall_list)

        if index != -1:
            return True

        else:
            return False
