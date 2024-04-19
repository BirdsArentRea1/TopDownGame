import pygame
import random

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
ticker = 0
py = 0
px = 0

class enemy:
    def __init__(self):
        self.xpos = 400
        self.ypos = 200
        self.direction = RIGHT
#wander
    def move(self):
        if ticker % 40 == 0:
            num = random.randrange(0,4)
            if num == 0:
                self.direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction = UP
            elif num == 3:
                self.direction = DOWN

#check for player
        if abs(int(py/50) - int(self.ypos/50))<2:
            if px < self.xpos:
                self.xpos-=5
                self.direction = LEFT
            else:
                self.xpos+=5
                self.direction = RIGHT
        if abs(int(px/50) - int(self.xpos/50))<2:
            if py < self.ypos:
                self.ypos-=5
                self.direction = LEFT
            else:
                self.ypos+=5
                self.direction = RIGHT

#wall collision
        if self.direction == RIGHT and map[int((self.ypos ) /50)][int ( (self.xpos + 20) /50 )] ==2:
            print("collision right")
            self.direction = UP
            self.xpos -= 6
        if self.direction == LEFT and map[int((self.ypos ) /50)][int ( (self.xpos - 20) /50 )] ==2:
            print("collision left")
            self.direction = DOWN
            self.xpos += 6
        if self.direction == UP and map[int((self.ypos ) /50)][int ( (self.xpos + 20) /50 )] ==2:
            print("collision up")
            self.direction = LEFT
            self.xpos += 6
        if self.direction == DOWN and map[int((self.ypos ) /50)][int ( (self.xpos - 20) /50 )] ==2:
            print("collision down")
            self.direction = RIGHT
            self.xpos += 6

#move
        if self.direction == RIGHT:
            self.xpos += 3
        if self.direction == LEFT:
            self.xpos -= 3
        if self.direction == UP:
            self.xpos += 3
        if self.direction == DOWN:
            self.xpos -= 3
        e1.move(map, ticker, p1.xpos, p1.ypos)


    def draw(self,screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xpos, self.ypos, 30, 30))
