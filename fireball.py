import pygame
import math
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

class fireball:
    def __init__(self):
        self.xpos = -10
        self.ypos = -10
        self.vx = 0
        self.vy = 0

        self.isAlive = False
        self.direction = RIGHT

    def shoot(self, x, y, dir):
        self.xpos = x + 20
        self.ypos = y + 20
        self.isAlive = True
        self.direction = dir

    def move(self):
        if self.direction == RIGHT:
            self.xpos+=20
        elif self.direction == LEFT:
            self.xpos-=20
        if self.direction == DOWN:
            self.ypos-=20
        elif self.direction == UP:
            self.ypos+=20

    def draw(self, screen):
        pygame.draw.circle(screen, (250, 0, 0), (self.xpos, self.ypos), 10)
        pygame.draw.circle(screen, (250, 250, 0), (self.xpos, self.ypos), 5)

    def collide(self, x, y):
        if math.sqrt((self.xpos - x) ** 2 + (self.ypos - y) ** 2) < 25:
            print("collision!")
            return True
        else:
            return False
