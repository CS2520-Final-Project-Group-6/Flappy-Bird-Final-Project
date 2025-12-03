import pygame
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() #initialize Sprite superclass to use methods such as group

        self.image = pygame.image.load('assets/images/up_pipe.png')