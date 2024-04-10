import pygame

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

class player:
    def __init__(self):

        self.xpos = 400
        self.ypos = 415
        self.vx = 0
        self.vy = 0
        

    def draw(self,screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))

    def move(self, keys, map):
        if keys[LEFT] == True:
            self.vx = -3
            print("left")
        elif keys[RIGHT] == True:
            self.vx = 3
            print("right")
        

        else:
            self.vx = 0
        if keys[UP] == True:
            self.vy = -3
            print("up")
        elif keys[DOWN] == True:
            self.vy = 3
            print("down")
        else:
            self.vy = 0
        if map[int((self.ypos- 10) / 50 )][int((self.xpos - 10) / 50)] == 2:
            self.xpos+=3

        if map[int((self.ypos-10) / 50 )][int((self.xpos + 30 + 5) / 50)] == 2:
            self.xpos-=3

        if map[int((self.ypos -5) / 50 )][int((self.xpos) / 50)] == 2:
            self.ypos+=3

        if map[int((self.ypos+ 30 + 5) / 50 )][int((self.xpos ) / 50)] == 2:
            self.ypos-=3
 
        self.xpos+=self.vx
        self.ypos+=self.vy
