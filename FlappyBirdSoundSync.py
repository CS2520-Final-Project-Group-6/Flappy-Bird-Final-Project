#Sets Up Pygame
import pygame
from pygame.locals import *
import time


pygame.mixer.init()


flapSound = pygame.mixer.Sound("/Users/ashishbogati/Downloads/244980__ani_music__wing-flap-flag-flapping-7a.wav")

#Plays a flapping sounds audio function
def flapping():
    flapSound.play()
≠
#Loop's through when an event happnes and if that event is a space down then it will play a flapping sound and jump. 
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            jump() #Not Actice right now due to not being setup
            flapping()




