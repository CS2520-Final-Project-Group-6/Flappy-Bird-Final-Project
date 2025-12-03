import pygame

class button(pygame.sprite.Sprite):
    def __init__(self, x, y, game_state):
        super().__init__()

        self.image = pygame.image.load("assets/images/button.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200,100))
        self.rect = self.image.get_rect(midbottom = (x/2,y/2))

    def getRect(self):
        return self.rect


