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
        self.status = "c"
        self.switchBtn = pygame.Rect(10,10,100,30)
    
    def displayMap(self,account2):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((32*20+outline*2, 32*20+outline*2+header+10))
        pygame.display.set_caption("Battle Ship")
        icon = pygame.image.load("client/game/assets/icon.png")
        pygame.display.set_icon(icon)

        font = pygame.font.SysFont("Arial", 14)
        font2 = pygame.font.SysFont("Arial", 20)
        

        

        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    print("quit")   
                    self.playing = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.onClick(pos)

            
            if not self.chosen:
                for i in range(0,20):
                    for j in range(0,20):
                        if self.blankMap[i][j] == "water":
                            screen.blit(water, (j*32+outline,i*32+outline + header+10))
                        if self.blankMap[i][j] == "full":
                            screen.blit(full, (j*32+outline,i*32+outline + header+10))
                        if self.blankMap[i][j] == "hit":
                            screen.blit(hit, (j*32+outline,i*32+outline + header+10))
                        if self.blankMap[i][j] == "missed":
                            screen.blit(missed, (j*32+outline,i*32+outline + header+10))
                        
            else:
                for i in range(0,20):
                    for j in range(0,20):
                        if self.myMap[i][j] == "water":
                            screen.blit(water, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "full":
                            screen.blit(full, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "hit":
                            screen.blit(hit, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "missed":
                            screen.blit(missed, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship1":
                            screen.blit(ship1, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship2":
                            screen.blit(ship2, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship3":
                            screen.blit(ship3, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship4":
                            screen.blit(ship4, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship5":
                            screen.blit(ship5, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship6":
                            screen.blit(ship6, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship7":
                            screen.blit(ship7, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship8":
                            screen.blit(ship8, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship9":
                            screen.blit(ship9, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship10":
                            screen.blit(ship10, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship11":
                            screen.blit(ship11, (j*32+outline,i*32+outline + header+10))
                        if self.myMap[i][j] == "ship12":
                            screen.blit(ship12, (j*32+outline,i*32+outline + header+10))
            screen.fill((15, 54, 105))

            pygame.draw.rect(screen, (255,255,255),self.switchBtn)
            switchScreenText = font.render("Switch Screen" , True, (15, 54, 105))
            width,height = pygame.font.Font.size(font, "Switch Screen")
            screen.blit(switchScreenText, (self.switchBtn.centerx-width/2, self.switchBtn.centery-height/2))


            statusText = font2.render("This is your turn", True, (255, 255, 255))
            if self.waiting:
                statusText = font2.render("Waiting for your turn", True, (255, 255, 255))
            width,height = pygame.font.Font.size(font2, "This is your turn")
            if self.waiting:
                width,height = pygame.font.Font.size(font2, "Waiting for your turn")
            screen.blit(statusText, (screen.get_width()/2-width/2,10+ 30/2-height/2))

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


