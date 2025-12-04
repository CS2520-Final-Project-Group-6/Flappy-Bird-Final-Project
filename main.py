import pygame
import math
from bird_class import Bird
import pipes_classj
import game_states
from menu_class import button, buttonWithText

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

buttonHeight = 50
buttonWidth = 225

#create menu
buttonStart = buttonWithText(sc_width/2,sc_height/3, buttonWidth, buttonHeight, game_states.in_game, "Start Game", 30)
buttonQuit = buttonWithText(sc_width/2,sc_height/2, buttonWidth, buttonHeight, game_states.run, "Quit Game", 30)
menu_group = pygame.sprite.Group()
menu_group.add(buttonStart)
menu_group.add(buttonQuit)



while game_states.run:
    #end game when pressing 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_states.run = False

        


    clock.tick(FPS)

    #draw scrolling background

    for i in range(0, tiles):
        # current tile *  background width + scrolling
        screen.blit(bg,(i * bg_width + scroll, 0))

    #separate scroll for the ground, it will scroll faster than the bg
    for i in range (0, grTiles):
        screen.blit(scaledGR, (i * gr_width + gr_scroll, 419))


    
    scroll -= 0.5  # half a pixel to the left per frame
    gr_scroll -= 5 #5 pixels to the left per frame

    #reset the scrolling
    #when scroll's absolute value is less than the background width, reset to 0
    if abs(scroll) > bg_width:
        scroll = 0

    #when ground scroll's abs value is less than the ground width, reset to 0
    if abs(gr_scroll) > gr_width:
        gr_scroll = 0
    
    #check game state if in game, show bird and update, else show menu
    if game_states.in_game:
        bird_group.draw(screen) #put the sprite in the game window
        bird_group.update()
        if game_states.fail: #take you back to menu if you fail
            game_states.in_game = False
            
    else:
        menu_group.draw(screen) #if not in game then show the menu
        menu_group.update()
        #if you failed and are in the menu, reset fail state and create new bird in original position
        #Can change the order of this later if needed(show different menu on fail vs quit to menu)
        if game_states.fail:
            game_states.fail = False
            newBird = Bird(200, 228) #create a new bird instance
            bird_group.add(newBird) #reset bird position by adding a new bird to the group



    pygame.display.update()

pygame.quit()
