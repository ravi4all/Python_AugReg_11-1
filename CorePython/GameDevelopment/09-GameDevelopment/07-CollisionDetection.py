# Import pygame module
import pygame
import random

# Initialize pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = 0,0,0

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

x = 0
y = 0

move_x = 0
move_y = 0

clock = pygame.time.Clock()
FPS = 40

enemy_x = random.randint(0,width)
enemy_y = random.randint(0,height)

while True:

    # Event Handling
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = +5
                move_y = 0
            if event.key == pygame.K_LEFT:
                move_x = -5
                move_y = 0
            if event.key == pygame.K_UP:
                move_y = -5
                move_x = 0
            if event.key == pygame.K_DOWN:
                move_y = +5
                move_x = 0

    screen.fill(white)

    rect_1 = pygame.draw.rect(screen, red,[x,y,50,50])
    rect_2 = pygame.draw.rect(screen, black,[enemy_x, enemy_y, 50, 50])

    x += move_x
    y += move_y

    if rect_1.colliderect(rect_2):
        enemy_x = random.randint(0,width)
        enemy_y = random.randint(0,height)

    pygame.display.update()
    clock.tick(FPS)
