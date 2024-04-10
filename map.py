import pygame
from player import player
pygame.init()
pygame.display.set_caption("top down game")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
gameover = False

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

p1 = player()

keys = [False, False, False,False]

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,2,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,2,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

brick = pygame.image.load('piskelstonebricks.png')
floor = pygame.image.load('piskelwoodplanks.png')

while not gameover:#GAMELOOP############################################################################################################
    clock.tick(60)
#INPUT----------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            if event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            if event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False

    #PHYSICS--------------------------------------------------------------------------------------------------------------------------------
    p1.move(keys, map)
    #RENDER---------------------------------------------------------------------------------------------------------------------------------

    screen.fill((0,0,0))

    for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    screen.blit(floor, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 2:
                    screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))

    p1.draw(screen)

    pygame.display.flip()

#GAME LOOP END##########################################################################################################################
pygame.quit()
