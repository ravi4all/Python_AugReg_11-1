import pygame

pygame.init()

speed = [2,2]

white = 255,255,255

size = width, height = 900,600

screen = pygame.display.set_mode(size)

img = pygame.image.load("ball.jpg")
img_rect = img.get_rect()

music = pygame.mixer.music.load("hit.wav")
play_music = pygame.mixer.music

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    img_rect = img_rect.move(speed)

    if img_rect.left < 0 or img_rect.right > width:
        speed[0] = -speed[0]
        play_music.play(1)
    elif img_rect.top < 0 or img_rect.bottom > height:
        speed[1] = -speed[1]
        play_music.play(1)


    screen.fill(white)
    screen.blit(img,img_rect)


    pygame.display.update()
