import pygame
import sys
from createMap import createMap
from test import *
#khoi tao pygame
pygame.init()

#tao man hinh
screen = pygame.display.set_mode((32*20+20, 32*20+20))

#icon and title
pygame.display.set_caption("Battle Ship")
icon = pygame.image.load("assets/battleship.png")
pygame.display.set_icon(icon)


#Game Loop                                                               

running = True
atlas = []
createMap(atlas)


def handle_mouse_click(atlas,pos):
    for i in atlas:
        for j in i:
            if j["pos"][0] < pos[0] < j["pos"][0] + 30 and j["pos"][1] < pos[1] < j["pos"][1] + 30:
                j["sprite"] = pygame.transform.scale(pygame.image.load("assets/cancel.png"),(30,30))

z = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            handle_mouse_click(atlas,pos)
    pygame.display.update()
    screen.fill((19, 90, 18  ))
    t = input("nhap: ")
    print(t)
    drawGrid(20)
    for i in atlas:
        for j in i:
            screen.blit(j["sprite"], j["pos"])
    pygame.display.update()

