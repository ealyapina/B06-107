import pygame
from pygame.draw import *
pygame.init()

screen = pygame.display.set_mode((1200, 800))

screen.fill(pygame.Color('#88AA88'))

line(screen, pygame.Color('#DB7093'), (320, 580), (320, 700), 30)
line(screen, pygame.Color('#DB7093'), (480, 580), (480, 700), 30)
circle(screen, pygame.Color('#FFC0CB'), (400, 400), 200)
circle(screen, pygame.Color('#FF1493'), (400, 400), 200, 5)
polygon(screen, pygame.Color('#FF1493'), [(310, 310), (310, 350), (350, 310)], 5)
polygon(screen, pygame.Color('#FF1493'), [(490, 310), (490, 350), (450, 310)], 5)
circle(screen, pygame.Color('#FFC0CB'), (400, 400), 100)
circle(screen, pygame.Color('#FF1493'), (400, 400), 100, 3)
circle(screen, pygame.Color('#FFC0CB'), (400, 430), 30)
circle(screen, pygame.Color('#FF1493'), (400, 430), 30, 1)
circle(screen, (1,1,1), (410,430), 10)
circle(screen, (1,1,1), (390,430), 10)
circle(screen, (0, 255, 255),
       (370,370), 20)
circle(screen, (0, 255, 255),
       (430,370), 20)
circle(screen, (0, 1, 1),
       (370,370), 10)
circle(screen, (0, 1, 1),
       (430,370), 10)
line(screen, pygame.Color('#DB7093'), (370, 470), (430, 470), 10)

pygame.display.update()

newSurf = pygame.Surface((1200, 800))
newSurf.set_colorkey((0,0,0))
line(newSurf, pygame.Color('#DB7093'), (320, 580), (320, 700), 30)
line(newSurf, pygame.Color('#DB7093'), (480, 580), (480, 700), 30)
circle(newSurf, pygame.Color('#FFC0CB'), (400, 400), 200)
circle(newSurf, pygame.Color('#FF1493'), (400, 400), 200, 5)
polygon(newSurf, pygame.Color('#FF1493'), [(310, 310), (310, 350), (350, 310)], 5)
polygon(newSurf, pygame.Color('#FF1493'), [(490, 310), (490, 350), (450, 310)], 5)
circle(newSurf, pygame.Color('#FFC0CB'), (400, 400), 100)
circle(newSurf, pygame.Color('#FF1493'), (400, 400), 100, 3)
circle(newSurf, pygame.Color('#FFC0CB'), (400, 430), 30)
circle(newSurf, pygame.Color('#FF1493'), (400, 430), 30, 1)
circle(newSurf, (1,0,0), (410,430), 10)
circle(newSurf, (1,0,0), (390,430), 10)
circle(newSurf, (0, 255, 255),
       (370,370), 20)
circle(newSurf, (0, 255, 255),
       (430,370), 20)
circle(newSurf, (0, 1, 1),
       (370,370), 10)
circle(newSurf, (0, 1, 1),
       (430,370), 10)
line(newSurf, pygame.Color('#DB7093'), (370, 470), (430, 470), 10)

newnewSurf = pygame.transform.scale(newSurf, (300, 200))
screen.blit(newnewSurf, (800, 600))
newnewSurf1 = pygame.transform.scale(newSurf, (600, 400))
screen.blit(newnewSurf1, (800, 100))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
