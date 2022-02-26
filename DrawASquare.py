import pygame
import math
import random

Running = True

pygame.init()
pygame.display.set_caption("Squares")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
clock = pygame.time.Clock()

class Square:
    def __init__(self, xpos, ypos, scale, dilation = 2):
        self.xpos = xpos
        self.ypos = ypos
        self.scale = scale
        self.dilation = dilation
        self.UP = True

        self.distance = math.sqrt(((self.dilation * math.pow(self.scale, 2)) - (math.pow(self.scale, 2)))) #these are the same
        self.distance = abs(self.scale)

    def draw(self, color):
        screen.fill((0,0,0))
        pygame.draw.lines(screen, color, True, [(self.xpos - self.scale, self.ypos + self.distance),(self.xpos + self.scale, self.ypos + self.distance),(self.xpos + self.scale, self.ypos - self.distance),(self.xpos - self.scale, self.ypos - self.distance)], 5)
        pygame.display.flip()
        if self.UP == True:
            if self.scale <= 400:
                self.scale += .1
            else:
                self.UP = False
        else:
            if self.scale >= 0:
                self.scale -= .1
            else:
                self.UP = True
        self.distance = math.sqrt(((self.dilation * math.pow(self.scale, 2)) - (math.pow(self.scale, 2))))


s1 = Square(400,400,20)

Squares = []
for i in range(20):
    Squares.append(Square(400,400,i * 20))

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    # color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # for i in Squares:
    #     i.draw(color)
    s1.draw((255,0,0))
pygame.quit()