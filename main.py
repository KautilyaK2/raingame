import pygame
import random
pygame.init()
win=pygame.display.set_mode((800,800))
p=0.3
cells=[[int(random.random()<p) for i in range(20)] for j in range(20)]
cell_size=800//20
cell = pygame.Surface((cell_size,cell_size)) 
cell = cell.convert() 
cell.fill((255, 0, 0)) 
done=0
px,py=0,0
health=10
maxhealth=10
f=0
font = pygame.font.SysFont('Comic Sans MS', 30)
def nextlevel(p):
    p=p-0.05
    cells=[[int(random.random()<p) for i in range(20)] for j in range(20)]
    return cells
while not done:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                py-=cell_size
            if event.key==pygame.K_DOWN:
                py+=cell_size
            if event.key==pygame.K_LEFT:
                px-=cell_size
            if event.key==pygame.K_RIGHT:
                px+=cell_size
        if event.type==pygame.QUIT:
             done=1
    win.fill((0,0,0))
    text_surface = font.render(str(int(health)), False, (0, 0, 0))
    print(cells[px//cell_size][py//cell_size])
    if cells[py//cell_size][px//cell_size]==0:
        health-=0.01
        f=0
    else:
        if not f:
            maxhealth+=0.25
        if health<maxhealth:
            health+=0.01
        else:
            health=maxhealth
        f=1
    if px==py==800-cell_size:
        maxhealth=health
        cells=nextlevel(p)
        px,py=0,0
    for y in range(len(cells)): 
            for x in range(len(cells[y])): 
                if cells[y][x]==1: 
                    win.blit(cell,(cell_size*x,cell_size*y)) 
    pygame.draw.rect(win,(0,255,0),pygame.Rect(px,py,cell_size,cell_size))
    win.blit(text_surface,(px,py))
    pygame.display.flip()