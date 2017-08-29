import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500))

red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
col = red

gameLoop = True

while gameLoop:

    screen.fill(col)

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            gameLoop = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            col = green
        else:
            col = red

    pygame.draw.rect(screen, black, (10,10,100,100))

    pygame.display.update()


quit()
