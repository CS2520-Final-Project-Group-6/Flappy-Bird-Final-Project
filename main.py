import pygame
import math
from bird_class import Bird
import pipes_classj

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
bg = pygame.image.load("assets/images/bg.png").convert()

#define game variables
scroll = 0 #variable for horizontal movement
bg_width = bg.get_width()

#image doesn't actually fit the window size, so calculate the number of
#duplicate images to fill the window
tiles = math.ceil(sc_width / bg_width) + 1

#create a bird
newBird = Bird(200, 228)
bird_group = pygame.sprite.Group()
bird_group.add(newBird)



flying = False #initial state

run = True
while run:

    clock.tick(FPS)

    #draw scrolling background

    for i in range(0, tiles):
        # current tile *  background width + scrolling
        screen.blit(bg,(i * bg_width +scroll, 0))

    bird_group.draw(screen) #put the sprite in the game window

    bird_group.update(flying) #pass in true so that the bird can start jumping

    scroll -= 1 #2 pixels to the left per frame

    #reset the scrolling
    #when scroll's absolute value is less than the background width, reset
    if abs(scroll) > bg_width:
        scroll = 0

    #end game when pressing 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #starts the game when 'space' is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flying = True

    pygame.display.update()

pygame.quit()
