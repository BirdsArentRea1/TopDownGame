import pygame
from player import player
from fireball import fireball
from enemy import enemy
pygame.init()
pygame.display.set_caption("top down game")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
gameover = False
#☻
die = pygame.mixer.Sound('LegoYodaDeath.mp3')
boom = pygame.mixer.Sound('VineBoom.mp3')
warp = pygame.mixer.Sound("smb_pipe.wav")

xpos= 500 
ypos = 200 
vx = 0 
keys = [False, False, False, False] 

xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits, 4 is quit, 5 is death screen
button1 = False
button2 = False
button3 = False
quitGame = False

#CONSTANTS
LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5
ticker = 0
#instantiate a player
p1 = player()
e1 = enemy()
ball = fireball()

keys = [False, False, False,False,False]

mapNum = 1

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2], 
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,5],
       [2,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

map2 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2], 
       [2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2],
       [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

map3 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2], 
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

brick = pygame.image.load('piskelstonebricks.png')
floor = pygame.image.load('piskelwoodplanks.png')

while not gameover:#GAMELOOP############################################################################################################
    clock.tick(60)
    ticker += 1
#INPUT----------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            if event.key == pygame.K_SPACE:
                keys[SPACE] = False
                
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                quitGame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                quitGame = False

    #PHYSICS--------------------------------------------------------------------------------------------------------------------------------
    print(mousePos)
    if mapNum == 1:
        p1.move(keys, map)
    elif mapNum == 2:
        p1.move(keys, map2)
    elif mapNum == 3:
        p1.move(keys, map3)
    if mapNum == 1 or 2 or 3:
        if e1.isAlive == True:
            e1.move(map, ticker, p1.xpos, p1.ypos)
            e1.die(ball.xpos, ball.ypos)
            p1.ouch(e1.xpos, e1.ypos)

    #if e1.die == True:
        #pygame.mixer.Sound.play(boom)
    
    if p1.health <= 0:
        state = 5
    #move between maps 1-2
    if mapNum == 1:
        if map[int((p1.ypos)/50)][int((p1.xpos)/50)] == 5:
            mapNum = 2
            pygame.mixer.Sound.play(warp)
            p1.xpos = 50
    if mapNum == 2:
        if map2[int((p1.ypos)/50)][int((p1.xpos)/50)] == 5:
            mapNum = 1
            pygame.mixer.Sound.play(warp)
            p1.xpos = 930


    #move between 2-3
    if mapNum == 2:
        if map2[int((p1.ypos)/50)][int((p1.xpos)/50)] == 6:
            mapNum = 3
            pygame.mixer.Sound.play(warp)
            p1.xpos = 50
    if mapNum == 3:
        if map3[int((p1.ypos)/50)][int((p1.xpos)/50)] == 6:
            mapNum = 1
            pygame.mixer.Sound.play(warp)
            p1.xpos = 930
    if ball.isAlive == True:
        ball.move()
    if keys[SPACE] == True:
            ball.shoot(p1.xpos, p1.ypos, p1.direction)

    #state 1: menu state!------------------------------
    if state == 1 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False
        
    if state == 1 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<600:
        button2 = True
    else:
        button2 = False
        
    if state == 1 and mousePos[0]>700 and mousePos[0]<898 and mousePos[1]>400 and mousePos[1]<600:
        button3 = True
    else:
        button3 = False
            
    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    
    if state == 1 and button2 == True and mouseDown == True:
        state = 3
        
    if state == 1 and button3 == True and mouseDown == True:
        state = 4
    #state 2: playing state!---------------------------
    if state == 2 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    if state == 3 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    if state == 4 and quitGame == True: #pressing quit takes you back to menu
        state = 1

    #RENDER---------------------------------------------------------------------------------------------------------------------------------

    screen.fill((0,0,0))

    if state == 1:
        screen.fill((230,100,100))# Clear the screen pink
        #have more text here for buttons and whatnot
        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150)) #dark green            
        else:
            pygame.draw.rect(screen, (200, 250, 200), (100, 400, 200, 150))#light green
            
        if button2 == False:
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (400, 400, 200, 150))
            
        #repeat for third button
        if button3 == False:
            pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (700, 400, 200, 150))

       
    #game state-------------------------------
    if state == 2:
        if mapNum == 1:
            screen.fill((80,150,100))# Clear the screen green
            for i in range(len(map)):
                for j in range(len(map[i])):
                    if map[i][j] == 1:
                        screen.blit(floor, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 5:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))

        elif mapNum == 2:
            screen.fill((80,150,100))
            for i in range(len(map2)):
                for j in range(len(map2[i])):
                    if map2[i][j] == 1:
                        screen.blit(floor, (j * 50, i * 50), (0, 0, 50, 50))
                    if map2[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map2[i][j] == 5:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                    if map2[i][j] == 6:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))

        elif mapNum == 3:
            screen.fill((80,150,100))
            for i in range(len(map3)):
                for j in range(len(map2[i])):
                    if map3[i][j] == 1:
                        screen.blit(floor, (j * 50, i * 50), (0, 0, 50, 50))
                    if map3[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map3[i][j] == 5:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                    if map3[i][j] == 6:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                
        p1.draw(screen)
        e1.draw(screen)
        if ball.isAlive == True:
            ball.draw(screen)
        
         #health bar
        pygame.draw.rect(screen, (255, 255, 255), (750, 5, 200, 30))
        pygame.draw.rect(screen, (150, 0, 0), (750, 5, p1.health, 30))
        pygame.draw.rect(screen, (0,0,0), (750, 5, 200, 30), 3)
    
    #if state == 3:
        #screen.fill((64,224,208))# clear the screen turquoise
        
    #if state == 4:
        #screen.fill((139,0,0))#clear the screen darkred

    if state == 5:
        screen.fill((250,0,0))
        pygame.mixer.Sound.play(die)

    pygame.display.flip()

#GAME LOOP END##########################################################################################################################
pygame.quit()
