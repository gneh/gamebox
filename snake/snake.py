# -*- coding: utf-8 -*-
import sys
import pygame
import time
from pygame.locals import *
from base import *

pygame.init()

SCREEN_X, SCREEN_Y = 600, 500
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

map = Map(SCREEN_X, SCREEN_Y)

# myfont = pygame.font.Font(None, 60)

snake_color = 255, 255, 255
snake_head_color = 255, 0, 255
food_color = 0, 255, 255
background = 0, 0, 255
# textImage = myfont.render("Hello Pygame!", True, white)

while True:
    for event in pygame.event.get(KEYUP):
        if event.key == K_d:
            map.change_direction('R')
        if event.key == K_a:
            map.change_direction('L')
        if event.key == K_w:
            map.change_direction('U')
        if event.key == K_s:
            map.change_direction('D')
        if event.key == K_e:
            map.eat()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    map.move()
    screen.fill(background)
    positions = map.get_positions()
    pygame.draw.rect(screen, snake_head_color, positions[0])
    pygame.draw.circle(screen, food_color, map.get_food_position(), map.width / 2)
    del positions[0]
    for position in positions:
        pygame.draw.rect(screen, snake_color, position)
    map.isEat()
    pygame.display.update()
    time.sleep(0.1)