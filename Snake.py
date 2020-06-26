import pygame
from random import randint
from math import log
from time import sleep

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
random_color = (randint(0,255),randint(0,255),randint(0,255))

try:
    pygame.init()
except:
    print("Erro iniciando o PyGame")

width = 400
height = 400
size = 20



clock = pygame.time.Clock()
background = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None,25)

def text(msg,color,pos_x,pos_y):
    text = font.render(msg,True,color)
    background.blit(text,[pos_x,pos_y])
    pygame.display.update()
    

def snake(SnakeXY):
    for XY in SnakeXY:
        pygame.draw.rect(background,white,[XY[0],XY[1],size,size])

def apple(pos_x,pos_y):
    pygame.draw.rect(background,(randint(0,255),randint(0,255),randint(0,255)),[pos_x,pos_y,size,size])

def game():
    sair = False
    pos_x = randint(0,(width-size)/size)*size
    pos_y = randint(0,(height-size)/size)*size
    
    target_x = randint(0,(width-size)/size)*size
    target_y = randint(0,(height-size)/size)*size
    
    
    speed_x = 0
    speed_y = 0
    
    SnakeXY = []
    score = 10
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and speed_x == 0:
                    speed_y = 0
                    speed_x = -1
                    break
                if event.key == pygame.K_RIGHT and speed_x == 0:
                    speed_y = 0
                    speed_x = 1
                    break
                if event.key == pygame.K_UP and speed_y == 0:
                    speed_x = 0
                    speed_y = -1
                    break
                if event.key == pygame.K_DOWN and speed_y == 0:
                    speed_x = 0
                    speed_y = 1
                    break
                    
        pos_x += speed_x*size
        pos_y += speed_y*size
                
        if pos_x >= width:
            pos_x -= width
        elif pos_x <= -size:
            pos_x += width
        elif pos_y >= height:
            pos_y -= height
        elif pos_y <= -size:
            pos_y += height
        
        if pos_x == target_x and pos_y == target_y:
             target_x = randint(0,(width-size)/size)*size
             target_y = randint(0,(height-size)/size)*size
             score += 1
        
        background.fill(black)
        apple(target_x,target_y)
        
        
        SnakeStart = []
        SnakeStart.append(pos_x)
        SnakeStart.append(pos_y)
        if SnakeStart in SnakeXY[:-1] and score > 0:
            text("A cobra morreu. Score: " + str(score),red,width/4,height/2)
            sleep(5)
            score = 0
            speed_x = 0
            speed_y = 0
            

        
        if len(SnakeXY)>0:
            if SnakeXY[-1] != SnakeStart:
                SnakeXY.append(SnakeStart)
        else:
            SnakeXY.append(SnakeStart)
        #print(len(SneakXY),score)
        #print(SneakXY)
        
        for i in range(2):
            if len(SnakeXY) > score+1:
                del(SnakeXY[0])
        
        
    
        snake(SnakeXY)
        pygame.display.update()
        clock.tick(5+log(1+score)**2)
    pygame.quit()

game()