import pygame



Map = {
    "ngang":20,
    "doc":20
}
soLuongTau = 12
outline = 10
header = 30
water = pygame.transform.scale(pygame.image.load("client/game/assets/border.png"),(30,30))
hit = pygame.transform.scale(pygame.image.load("client/game/assets/hit.png"),(30,30))
full = pygame.transform.scale(pygame.image.load("client/game/assets/full.png"),(30,30))
missed = pygame.transform.scale(pygame.image.load("client/game/assets/missed.png"),(30,30))
ship1 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/1.png"),(30,30))
ship2 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/2.png"),(30,30))
ship3 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/3.png"),(30,30))
ship4 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/4.png"),(30,30))
ship5 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/5.png"),(30,30))
ship6 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/6.png"),(30,30))
ship7 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/7.png"),(30,30))
ship8 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/8.png"),(30,30))
ship9 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/9.png"),(30,30))
ship10 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/10.png"),(30,30))
ship11 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/11.png"),(30,30))
ship12 = pygame.transform.scale(pygame.image.load("client/game/assets/ship/12.png"),(30,30))



kichThuoc27 = {"dai":7,"rong":2}
kichThuoc25 = {"dai":5,"rong":2}
kichThuoc14 = {"dai":4,"rong":1}
kichThuoc12 = {"dai":2,"rong":1}
kichThuoc11 = {"dai":1,"rong":1}