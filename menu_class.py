import pygame
import game_states

# Button class - creates a button sprite that can be clicked to trigger events
class button(pygame.sprite.Sprite):
    def __init__(self, x = 0, y= 0,width=200, height=50, event=None):
        """Initialize button sprite with position, size, and event to trigger on click."""

        super().__init__()
        self.image = pygame.image.load("assets/images/button.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(midbottom = (x,y)) 
        self.event = event
    # Check for mouse click on button and trigger associated event
    def clickButton(self):
        mous_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mous_pos):
            mouseclick = pygame.mouse.get_pressed()
            if mouseclick[0] == True:
                #If the event is to start the game or quit, set the appropriate game state variable
                if self.event == game_states.in_game:
                    game_states.in_game = True
                elif self.event == game_states.run:
                    game_states.run = False
    # Update method to be called in the game loop
    def update(self):
        self.clickButton()

# Button with Text subclass - adds text
class buttonWithText(button):
    """Button subclass that adds text rendering functionality."""

    def __init__(self, x=0, y=0, width=200, height=50, event=None, text="button", fontSize=30):
        super().__init__(x, y,width, height, event)
        self.text = text
        self.fontSize = fontSize

    # Render text onto the button
    def makeText(self):
        font = pygame.font.Font("assets/fonts/pixelfont.ttf", self.fontSize)
        textSurface = font.render(self.text, True, "Black")
        textRect = textSurface.get_rect(center=(self.rect.width/2, self.rect.height/2 - 5))
        self.image.blit(textSurface, textRect)

    # Update method to be called in the game loop
    def update(self):
        self.clickButton()
        self.makeText()