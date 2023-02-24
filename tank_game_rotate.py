import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('tanque.jpg').convert()
angle = 0
rotation = pygame.transform.rotate(tank, angle)

x,y=0,0
move_x, move_y = 0,0
speed = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                move_x=speed
            elif event.key==K_RIGHT:
                move_x=-speed
            elif event.key==K_UP:
                move_y=-speed
            elif event.key==K_DOWN:
                move_y=speed
        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_x=0
            elif event.key == K_RIGHT:
                move_x=0
            elif event.key == K_UP:
                move_y=0
            elif event.key == K_DOWN:
                move_y=0
    
    x += move_x
    y += move_y
    
    angle = (angle + move_x * 0.5) % 360
    rotation = pygame.transform.rotate(tank, angle)
    
    screen.fill((255,255,255))
    screen.blit(rotation, (x,y))

    pygame.display.update()
