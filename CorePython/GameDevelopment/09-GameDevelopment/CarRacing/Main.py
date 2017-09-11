# Import pygame module
import pygame
import random

# Initialize pygame
pygame.init()

white = (255,255,255)
green = (0,255,0)
gray = (140,140,140)
red = (255,0,0)

width = 800
height = 600

screen = pygame.display.set_mode((width,height))

road = pygame.image.load("assets/road.png")
road_2 = pygame.image.load("assets/road.png")

my_car = pygame.image.load("assets/my_car.png")
img_1 = pygame.image.load("assets/car_1.png")
img_2 = pygame.image.load("assets/car_2.png")
img_3 = pygame.image.load("assets/car_3.png")

opp_one_x = random.randint(200,width-200)
opp_two_x = random.randint(200,width-200)
opp_three_x = random.randint(200,width-200)

opp_one_y = -250
opp_two_y = -280
opp_three_y = -200

x = 0
y = 0

my_x = (width/2)-25
my_y = height-150

move_my_x = 0
move_bg = 0

clock = pygame.time.Clock()
FPS = 50

img_one_speed = 4
img_two_speed = 7
img_three_speed = 10

move_road_1 = 2
move_road_2 = -height

while True:

    # Event Handling
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_bg += 10
            elif event.key == pygame.K_DOWN:
                move_bg -= 10
            elif event.key == pygame.K_LEFT:
                move_my_x = -10
            elif event.key == pygame.K_RIGHT:
                move_my_x = +10

        if event.type == pygame.KEYUP:
            move_my_x = 0

    screen.fill(gray)

    pygame.draw.rect(screen, green,[x,y,150,height])
    pygame.draw.rect(screen, green,[width-150,y,200,height])

    screen.blit(road,[200,move_road_1])
    screen.blit(road_2,[200,move_road_2])

    screen.blit(my_car,[my_x, my_y])
    screen.blit(img_1, [opp_one_x, opp_one_y])
    screen.blit(img_2, [opp_two_x, opp_two_y])
    screen.blit(img_3, [opp_three_x, opp_three_y])

    opp_one_y += img_one_speed
    opp_two_y += img_two_speed
    opp_three_y += img_three_speed

    move_road_1 += move_bg
    move_road_2 += move_bg

    my_x += move_my_x
    

    if opp_one_y > height:
        opp_one_y = -250
        opp_one_x = random.randint(200,width-200)
    elif opp_two_y > height:
        opp_two_y = -250
        opp_two_x = random.randint(200,width-200)
    elif opp_three_y > height:
        opp_three_y = -250
        opp_three_x = random.randint(200,width-200)

    if move_road_1 > height:
        move_road_1 = -height
    elif move_road_2 > height:
        move_road_2 = -height

    pygame.display.update()
    clock.tick(FPS)
