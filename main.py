import pygame
import math
from bird_class import Bird
import pipes_classj


#main.py only contains the background scrolling
#objects from the bird and pipes class control the gameplay loop

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#window dimensions
sc_width = 800
sc_height = 457

#create game window
screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Flappy Bird")

#load images
bg = pygame.image.load("assets/images/bg.png").convert()
ground = pygame.image.load("assets/images/ground.png").convert()

scaledGR = pygame.transform.smoothscale(ground, (1479/7, 481/7)) #use scaled version as it fits the screen

#define game variables
scroll = 0 #variable for horizontal movement
gr_scroll = 0
bg_width = bg.get_width()
gr_width = scaledGR.get_width()


#image doesn't actually fit the window size, so calculate the number of
#duplicate images to fill the window, with a buffer of 1
tiles = math.ceil(sc_width / bg_width) + 1
grTiles = math.ceil(sc_width/gr_width) + 1

#create a bird
newBird = Bird(200, 228)
bird_group = pygame.sprite.Group()
bird_group.add(newBird)


#Control when the game starts
flying = False #initial state
run = True
while run:

    clock.tick(FPS)

    #draw scrolling background

    for i in range(0, tiles):
        # current tile *  background width + scrolling
        screen.blit(bg,(i * bg_width + scroll, 0))

    #separate scroll for the ground, it will scroll faster than the bg
    for i in range (0, grTiles):
        screen.blit(scaledGR, (i * gr_width + gr_scroll, 419))




    bird_group.draw(screen) #put the sprite in the game window

    #the bird object has a "fail" variable that is set to false.
    #While it's false aka the bird is still flying, the backgrounds will scroll.
    if not newBird.fail:
        bird_group.update(flying) #pass in true so that the bird can start jumping
        scroll -= 0.5  # half a pixel to the left per frame
        gr_scroll -= 5 #5 pixels to the left per frame


    #reset the scrolling
    #when scroll's absolute value is less than the background width, reset to 0
    if abs(scroll) > bg_width:
        scroll = 0

    #when ground scroll's abs value is less than the ground width, reset to 0
    if abs(gr_scroll) > gr_width:
        gr_scroll = 0


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
