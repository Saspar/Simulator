import pygame, sys
from constants import *
from math import floor

MAPX = screen_w // TILESIZE
MAPY = screen_h // TILESIZE

map1 = open("map_files/map1.data", "r")
map2 = open("map_files/map2.data", "r")
map1_width = int(map1.readline().strip())
map2_width = int(map2.readline().strip())
rectangle_list = []

tile_sheet = pygame.image.load("TILESHEET.png")

tiles = {
    "WALL_HORIZONTAL": tile_sheet.subsurface([300, 0, 50, 50]),
    "WALL_VERTICAL": tile_sheet.subsurface([250, 50, 50, 50]),
    "WALL_CORNER1": tile_sheet.subsurface([250, 0, 50, 50]),
    "WALL_CORNER2": tile_sheet.subsurface([350, 0, 50, 50]),
    "WALL_CORNER3": tile_sheet.subsurface([350, 100, 50, 50]),
    "WALL_CORNER4": tile_sheet.subsurface([250, 100, 50, 50]),
    "GRASS": tile_sheet.subsurface([300, 50, 50, 50]),
    "FLOOR": tile_sheet.subsurface([350, 150, 50, 50]),
    "TILES": tile_sheet.subsurface([300, 150, 50, 50]),
    "TABLE": tile_sheet.subsurface([100, 100, 50, 50]),

    "BED1_PILLOW": tile_sheet.subsurface([100, 0, 50, 50]),
    "BED1_MIDDLE": tile_sheet.subsurface([50, 0, 50, 50]),
    "BED1_BOTTOM": tile_sheet.subsurface([0, 0, 50, 50]),

    "BED2_PILLOW": tile_sheet.subsurface([100, 50, 50, 50]),
    "BED2_MIDDLE": tile_sheet.subsurface([50, 50, 50, 50]),
    "BED2_BOTTOM": tile_sheet.subsurface([0, 50, 50, 50]),

    "BED3_PILLOW": tile_sheet.subsurface([150, 0, 50, 50]),
    "BED3_MIDDLE": tile_sheet.subsurface([150, 50, 50, 50]),
    "BED3_BOTTOM": tile_sheet.subsurface([150, 100, 50, 50]),

    "BED4_PILLOW": tile_sheet.subsurface([200, 0, 50, 50]),
    "BED4_MIDDLE": tile_sheet.subsurface([200, 50, 50, 50]),
    "BED4_BOTTOM": tile_sheet.subsurface([200, 100, 50, 50]),


}


def read_map(map_data):
    map_list = []
    row = 0
    column = 0

    for line in map_data:
        map_list.append([])
        for letter in line:
            if letter == ' ':
                map_list[row].append(0)

            elif letter == '-':
                map_list[row].append(1)

            elif letter == 'C':
                map_list[row].append(2)

            elif letter == 'V':
                map_list[row].append(3)

            elif letter == 'P':
                map_list[row].append(4)

            elif letter == 'K':
                map_list[row].append(5)

            elif letter == 'W':
                map_list[row].append(6)

            elif letter == 'D':
                map_list[row].append(7)

            elif letter == 'R':
                map_list[row].append(8)

            elif letter == '1':
                map_list[row].append(9)

            elif letter == '2':
                map_list[row].append(10)

            elif letter == '3':
                map_list[row].append(11)

            elif letter == '4':
                map_list[row].append(12)

            elif letter == '|':
                map_list[row].append(13)

            elif letter == 'B':
                map_list[row].append(14)

            elif letter == 'N':
                map_list[row].append(15)

            elif letter == 'M':
                map_list[row].append(16)

            elif letter == ',':
                map_list[row].append(17)

        row += 1

    return map_list


def return_values(map, x1, x2, y):
    if y < 0 or y >= len(map):
        return [-1 for i in range(x2-x1)]

    elif x1 < 0:
        return [-1 for i in range(0 - x1)] + map[y][:x2]

    elif x2 >= len(map):
        return map[y][x1:] + [-1 for i in range(x2 - len(map) - 1)]

    else:
        return map[y][x1:x2]


map1_data = read_map(map1)


def get_rect_list():
    return rectangle_list


def draw(s, cam_pos):
    global rectangle_list

    tiles_x = screen_w // TILESIZE + 1
    tiles_y = screen_h // TILESIZE + 1

    cam_tiles_x = int(cam_pos[0] // TILESIZE)
    cam_tiles_y = int(cam_pos[1] // TILESIZE)

    cam_offset_x = int(cam_pos[0] % TILESIZE)
    cam_offset_y = int(cam_pos[1] % TILESIZE)

    subsection = [return_values(map1_data, cam_tiles_x, cam_tiles_x+tiles_x, j)
                  for j in range(cam_tiles_y, cam_tiles_y + tiles_y)]

    #print(subsection)

    rectangle_list = []

    for y, j in enumerate(subsection):
        for x, i in enumerate(j):
            rect = pygame.Rect([x * TILESIZE - cam_offset_x,
                                y * TILESIZE - cam_offset_y,
                                TILESIZE,
                                TILESIZE])

            if i != 0:
                rectangle_list.append(rect)

            if i == 0:
                s.blit(tiles["FLOOR"], rect)

            elif i == 1:
                s.blit(tiles["WALL_HORIZONTAL"], rect)

            elif i == 2:
                pygame.draw.rect(s, [255, 0, 0], rect)

            elif i == 3:
                s.blit(tiles["BED1_MIDDLE"], rect)

            elif i == 4:
                s.blit(tiles["BED1_PILLOW"], rect)

            elif i == 5:
                s.blit(tiles["TABLE"], rect)

            elif i == 6:
                s.blit(tiles["TILES"], rect)

            elif i == 7:
                pygame.draw.rect(s, [255, 114, 0], rect)

            elif i == 8:
                s.blit(tiles["GRASS"], rect)

            elif i == 9:
                s.blit(tiles["WALL_CORNER1"], rect)

            elif i == 10:
                s.blit(tiles["WALL_CORNER2"], rect)

            elif i == 11:
                s.blit(tiles["WALL_CORNER3"], rect)

            elif i == 12:
                s.blit(tiles["WALL_CORNER4"], rect)

            elif i == 13:
                s.blit(tiles["WALL_VERTICAL"], rect)

            elif i == 14:
                s.blit(tiles["BED2_MIDDLE"], rect)

            elif i == 15:
                s.blit(tiles["BED4_MIDDLE"], rect)

            elif i == 16:
                s.blit(tiles["BED3_MIDDLE"], rect)

            elif i == 17:
                s.blit(tiles["BED3_BOTTOM"], rect)
