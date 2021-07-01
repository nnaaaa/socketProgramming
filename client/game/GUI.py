import pygame
#khoi tao pygame
pygame.init()

#tao man hinh
screen = pygame.display.set_mode((32*20, 32*20))
#DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


#icon and title
pygame.display.set_caption("Battle Ship")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)


#Game Loop

chay = True
# if i["sprite"].get_rect().collidepoint(pos):
def handle_mouse_click(obj,pos):
    for i in obj:
        if i["pos"][0] < pos[0] < i["pos"][0] + 30 and i["pos"][1] < pos[1] < i["pos"][1] + 30:
            i["sprite"] = pygame.transform.scale(pygame.image.load("cancel.png"),(30,30))
a = []
for i in range(0,20):
    for j in range(0,20):
        image=pygame.image.load("waves.png")
        newSize = pygame.transform.scale(image,(30,30))
        a.append({
            "pos":(i*32,j*32),
            "sprite":newSize 
        })    

while chay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            chay = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            handle_mouse_click(a,pos)

    screen.fill((0, 0, 0))
    for i in a:
        screen.blit(i["sprite"], i["pos"])
    pygame.display.update()

pygame.display.flip()