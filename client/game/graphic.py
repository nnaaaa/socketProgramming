import pygame
from game.constants import *

class Atlas:
    def __init__(self,socket,account,myMap,blankMap,waiting):
        self.myMap = myMap
        self.blankMap = blankMap
        self.waiting = waiting
        self.playing = True
        self.socket = socket
        self.account = account
        self.chosen = waiting
        self.switchBtn = pygame.Rect(10,10,80,30)
    
    def displayMap(self,account2):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((32*20+outline*2, 32*20+outline*2+40))
        pygame.display.set_caption("Battle Ship")
        icon = pygame.image.load("client/game/assets/icon.png")
        pygame.display.set_icon(icon)

        font = pygame.font.SysFont("Arial", 11,bold=pygame.font.Font.bold)
        switchScreenText = font.render("Switch Screen" , True, (18, 66, 129))
        
        
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    self.playing = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.onClick(pos)

            screen.fill((18, 66, 129))
            if not self.chosen:
                for i in range(0,20):
                    for j in range(0,20):
                        if self.blankMap[i][j] == "water":
                            screen.blit(water, (j*32+outline,i*32+outline + 40))
                        if self.blankMap[i][j] == "full":
                            screen.blit(full, (j*32+outline,i*32+outline + 40))
                        if self.blankMap[i][j] == "hit":
                            screen.blit(hit, (j*32+outline,i*32+outline + 40))
                        if self.blankMap[i][j] == "missed":
                            screen.blit(missed, (j*32+outline,i*32+outline + 40))
                        if self.blankMap[i][j] == "tau11":
                            screen.blit(ship1, (j*32+outline,i*32+outline + 40))
                        if self.blankMap[i][j] == "tau14":
                            screen.blit(ship2, (j*32+outline,i*32+outline + 40))
                        if self.blankMap[i][j] == "tau25":
                            screen.blit(ship3, (j*32+outline,i*32+outline + 40))
                        if self.blankMap[i][j] == "tau27":
                            screen.blit(ship4, (j*32+outline,i*32+outline + 40))
            else:
                for i in range(0,20):
                    for j in range(0,20):
                        if self.myMap[i][j] == "water":
                            screen.blit(water, (j*32+outline,i*32+outline + 40))
                        if self.myMap[i][j] == "full":
                            screen.blit(full, (j*32+outline,i*32+outline + 40))
                        if self.myMap[i][j] == "hit":
                            screen.blit(hit, (j*32+outline,i*32+outline + 40))
                        if self.myMap[i][j] == "missed":
                            screen.blit(missed, (j*32+outline,i*32+outline + 40))
                        if self.myMap[i][j] == "tau11":
                            screen.blit(ship1, (j*32+outline,i*32+outline + 40))
                        if self.myMap[i][j] == "tau14":
                            screen.blit(ship2, (j*32+outline,i*32+outline + 40))
                        if self.myMap[i][j] == "tau25":
                            screen.blit(ship3, (j*32+outline,i*32+outline + 40))
                        if self.myMap[i][j] == "tau27":
                            screen.blit(ship4, (j*32+outline,i*32+outline + 40))
            pygame.draw.rect(screen, (255,255,255),self.switchBtn)
            screen.blit(switchScreenText, (self.switchBtn.x +5, self.switchBtn.y+5))
            pygame.display.update()
        pygame.display.flip()

    def onClick(self,pos):
        if pygame.Rect.collidepoint(self.switchBtn, pos):
            self.chosen = not self.chosen
        if self.waiting:
            return
        for i in range(0,20):
            for j in range(0,20):
                if j*32+outline < pos[0] < j*32+outline + 30 and i*32+outline + 30 < pos[1] < i*32+outline + 30 + 30:
                    if self.blankMap[i][j] == "water":
                        obj = {
                            "attack":True,
                            "position":{"x":j,"y":i} 
                        }
                        self.waiting = True
                        self.socket.send(bytes(str(obj),'utf8'))


