import pygame
import math
from bird_class import Bird
import pipes_classj
from menu_class import button

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

#create menu
in_game = False
#in_game - determines if we should be in-game
buttonStart = button(sc_width,sc_height,in_game)
menu_group = pygame.sprite.Group()
menu_group.add(buttonStart)

#create menu
in_game = False
#in_game - determines if we should be in-game
buttonStart = button(sc_width,sc_height,in_game)
menu_group = pygame.sprite.Group()
menu_group.add(buttonStart)



run = True
while run:
    #end game when pressing 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonStart.getRect().collidepoint(event.pos):
                in_game = True


    clock.tick(FPS)

    #draw scrolling background

    for i in range(0, tiles):
        # current tile *  background width + scrolling
        screen.blit(bg,(i * bg_width + scroll, 0))

    #separate scroll for the ground, it will scroll faster than the bg
    for i in range (0, grTiles):
        screen.blit(scaledGR, (i * gr_width + gr_scroll, 419))




    
    scroll -= 1 #2 pixels to the left per frame

    #reset the scrolling
    #when scroll's absolute value is less than the background width, reset to 0
    if abs(scroll) > bg_width:
        scroll = 0

    if in_game:
        bird_group.draw(screen) #put the sprite in the game window
        bird_group.update()
    else:
        menu_group.draw(screen)
        menu_group.update()



    pygame.display.update()

pygame.quit()
