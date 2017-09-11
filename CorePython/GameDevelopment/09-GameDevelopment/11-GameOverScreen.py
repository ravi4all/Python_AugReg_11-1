# Import pygame module
import pygame
import random

# Initialize pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = 0,0,0
green = 0,255,0

width = 800
height = 500

apple = pygame.image.load("asstes/image2.png")

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

pygame.mixer.init()
music_1 = pygame.mixer.Sound("asstes/smb_coin.wav")

def gameIntro():

    font_1 = pygame.font.SysFont("None",60)
    text_1 = font_1.render("Welcome to Snake Game", False, red)
    screen.blit(text_1,((width/2)-220,(height/2)-80))

    font_2 = pygame.font.SysFont("None",40)
    text_2 = font_2.render("Press S to start game", True, green)
    screen.blit(text_2,(230,300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainLoop()

        pygame.display.update()
    

def snake(snakeList):
    for s in snakeList:
        pygame.draw.rect(screen,black,[s[0],s[1],20,20])

def gameOverScreen():
    font = pygame.font.SysFont("None",60)
    text = font.render("Game Over", True, red)
    screen.blit(text,(width/2-60,height/2-30))

def count(counter):
    font = pygame.font.SysFont("None",30)
    text = font.render("Counter : "+str(counter), True, red)
    screen.blit(text,(20,20))


def mainLoop():

    x = 0
    y = 0

    snakeList = []
    snakeLength = 1

    move_x = 0
    move_y = 0

    enemy_x = random.randint(0,width-40)
    enemy_y = random.randint(0,height-40)

    counter = 0

    FPS = 10

    gameOver = False

    while not gameOver:

        # Event Handling
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = +20
                    move_y = 0
                if event.key == pygame.K_LEFT:
                    move_x = -20
                    move_y = 0
                if event.key == pygame.K_UP:
                    move_y = -20
                    move_x = 0
                if event.key == pygame.K_DOWN:
                    move_y = +20
                    move_x = 0

        screen.fill(white)

        rect_1 = [x,y,20,20]
        #rect_2 = pygame.draw.rect(screen, red,[enemy_x, enemy_y, 20, 20])

        screen.blit(apple, [enemy_x, enemy_y,])
        rect_2 = pygame.Rect(enemy_x, enemy_y,apple.get_width(),apple.get_height())
        
        x += move_x
        y += move_y

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        #print(snakeHead)
        snakeList.append(snakeHead)

        if len(snakeList) >  snakeLength:
            del(snakeList[0])

        snakeList[:-1]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                gameOverScreen()

        snake(snakeList)

        count(counter)

        if x > width or x < 0 or y > height or y < 0:
            gameOver = True
            gameOverScreen()

        pygame.display.update()

        if rect_2.colliderect(rect_1):
            enemy_x = random.randint(0,width)
            enemy_y = random.randint(0,height)
            snakeLength += 1
            counter += 1
            FPS += 1
            music_1.play(1)
        
        clock.tick(FPS)

#mainLoop()
gameIntro()
