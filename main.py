import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#window dimensions
sc_width = 800
sc_height = 457

#create game window
screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Flappy Bird")

#load image
bg = pygame.image.load("bg.png").convert()

#define game variables
scroll = 0 #variable for horizontal movement
bg_width = bg.get_width()

#image doesn't actually fit the window size, so calculate the number of
#duplicate images to fill the window
tiles = math.ceil(sc_width / bg_width) + 1

#game loop
run = True

while run:

    clock.tick(FPS)

    #draw scrolling background

    for i in range(0, tiles):
        # current tile *  background width + scrolling
        screen.blit(bg,(i * bg_width +scroll, 0))

    scroll -= 2 #2 pixels to the left per frame

    #reset the scrolling
    #when scroll's absolute value is less than the background width, reset
    if abs(scroll) > bg_width:
        scroll = 0

    #end game when pressing 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
