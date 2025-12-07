import pygame
#PHYSICS & GRAVITY FUNCTIONS
def gravity(self):
    """Handles the falling physics"""  #Docstring
    
    gravity = 0.5  #Every frame the bird falling speed increases by 0.5 pixels
    
    self.vel += gravity #Increases acceleration the longer falling
    
    self.rect.y += int(self.vel)   #Takes the current position and adds new speed to it
    
    #'int' converts decimal speed into whole numbers for computer to read nicely
    #'self.rect.y' is the vertical y-axis position of the bird sprite
    
def jump(self):
    """Handles user input for jumping"""  #Docstring
    
    #Checks if user presses left click on mouse (pushing the button down)
    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True  #Ensures one click equals one jump
        self.vel = -10  #Causes the bird's speed to shoot upward.
    
    #Checks if the user has let go of the mouse
    if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False  #Allows the 'self.clicked == False' check to work again

    
