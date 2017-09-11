# Import pygame module
import pygame

# Initialize pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)

screen = pygame.display.set_mode((800,500))

while True:

    # Event Handling
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    pygame.draw.rect(screen, red,[0,0,50,50])

    pygame.display.update()
