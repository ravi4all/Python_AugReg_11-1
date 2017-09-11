# Import pygame module
import pygame

# Initialize pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)

screen = pygame.display.set_mode((800,500))

x = 0
y = 0

move_x = 0
move_y = 0

clock = pygame.time.Clock()
FPS = 10

while True:

    # Event Handling
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x += 20
            if event.key == pygame.K_LEFT:
                move_x -= 20
            if event.key == pygame.K_UP:
                move_y -= 20
            if event.key == pygame.K_DOWN:
                move_y += 20

    screen.fill(white)

    pygame.draw.rect(screen, red,[x,y,50,50])

    x += move_x
    y += move_y

    pygame.display.update()
    clock.tick(FPS)
