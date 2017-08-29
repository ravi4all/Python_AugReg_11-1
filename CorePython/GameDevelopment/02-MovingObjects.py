import pygame

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))

red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
col = red

x = 10
y = 10

move_x = 0
move_y = 0

clock = pygame.time.Clock()
FPS = 20

gameLoop = True

while gameLoop:

    screen.fill(col)

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            gameLoop = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            col = green
        else:
            col = red

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 10
                move_y = 10
        # elif event.type == pygame.KEYUP:
        #     move_x = 0

    rect = pygame.draw.rect(screen, black, (x,y,100,100))

    x += move_x
    y += move_y

    # if rect.left > width:
    #     x = -100

    if rect.right > width:
        move_x = -10
    elif rect.bottom > height:
        move_y = -10
    elif rect.top < 0:
        move_y = 10
    elif rect.left < 10:
        move_x = 10


    pygame.display.update()
    clock.tick(FPS)

quit()
