import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() #initialize Sprite superclass to use methods such as group (will be used in main.py)

        #load sprites
        self.images = [
            pygame.image.load("redbird-midflap.png").convert(),
            pygame.image.load("redbird-downflap.png").convert(),
            pygame.image.load("redbird-upflap.png").convert()
                      ]
        self.index = 0 #which sprite from the list
        self.counter = 0 #control animation speed

        self.image = self.images[self.index] #represents the current sprite, in this case midflap
        self.rect = self.image.get_rect() #store position for collision, movement, etc.
        self.rect.center = [x, y] #initial position
        self.vel = 0
        self.clicked = False

    def update(self): #used to handle sprite animation and physics

        #MOVEMENT

        #gravity
        self.vel += 0.5
        if self.rect.bottom < 407: #stop movement once you hit the ground
            self.rect.y += int(self.vel)

        #prevent jumping above the screen
        if self.rect.top <=0:
            self.rect.top = 0

        ''' This is to let the bird jump off the ground but idk if that's allowed in the original game
        if self.rect.bottom >= 409:
            self.rect.bottom = 409
            self.vel = 0
        '''
            #jump
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked=True
            self.vel = -10

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #ANIMATION
        self.counter += 1
        flap_cooldown = 25

        #uses two variables to control animation speed
        #every 25 frames, the sprite changes
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1 #change to the next sprite in images[]

            #prevent out of bounds error
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        #test