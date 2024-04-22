import pygame

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

wizard = pygame.image.load('SpriteSheetWizard.png') 
wizard.set_colorkey((255, 0, 255)) 

class player:
    def __init__(self):

        self.xpos = 400
        self.ypos = 415
        self.vx = 0
        self.vy = 0
        self.direction = LEFT
        #animation variables variables
        self.frameWidth = 100
        self.frameHeight = 100
        self.RowNum = 2 
        self.frameNum = 0
        self.ticker = 0
        

    def draw(self,screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.xpos, self.ypos, 30, 30))

        screen.blit(wizard, (self.xpos, self.ypos), (self.frameWidth, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight)) 
    def move(self, keys, map):

        #movement algorithm--------------------------
        if keys[LEFT] == True:
            self.vx = -3
            self.RowNum = 0
            self.direction = LEFT
            print("left")
        elif keys[RIGHT] == True:
            self.vx = 3
            self.RowNum = 1
            self.direction = RIGHT
            print("right")
        

        else:
            self.vx = 0

        if keys[UP] == True:
            self.vy = 3
            self.RowNum = 3
            self.direction = UP
            print("up")
        elif keys[DOWN] == True:
            self.vy = -3
            self.RowNum = 2
            self.direction = DOWN
            print("down")
        else:
            self.vy = 0

        #collision------------------------------
        if map[int((self.ypos- 10) / 50 )][int((self.xpos - 10) / 50)] == 2:
            self.xpos+=3

        if map[int((self.ypos-10) / 50 )][int((self.xpos + 30 + 5) / 50)] == 2:
            self.xpos-=3

        if map[int((self.ypos -5) / 50 )][int((self.xpos) / 50)] == 2:
            self.ypos+=3

        if map[int((self.ypos+ 30 + 5) / 50 )][int((self.xpos ) / 50)] == 2:
            self.ypos-=3
 
        #update posistion
        self.xpos+=self.vx
        self.ypos+=self.vy


        if self.vx < 0 or self.vx > 0: #left animation
            self.ticker+=1
        if self.ticker%10==0: #only change frames every 10 ticks
          self.frameNum+=1
        if self.frameNum>7: 
           self.frameNum = 0
    
        if self.vy < 0 or self.vy > 0:
            self.ticker+=1
            if self.ticker%10==0: #only change frames every 10 ticks
                self.frameNum+=1
            if self.frameNum >7:
                self.frameNum = 0
