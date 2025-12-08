import pygame
import game_states
from sound_class import SoundManager

class ScoreManager:
    def __init__(self, screen_width, screen_height):
        self.score = 0        #Score of the player's current run
        self.high_score = 0   #Highest score of the player
        self.font = pygame.font.Font(r"assets\fonts\pixelfont.ttf", 60)  #Matches menu font
        self.color = (255, 255, 255)  #White text
        
        #Center the score at the top
        self.pos_x = screen_width / 2
        self.pos_y = screen_height / 5
        
        #Connecting the Sound Manager
        self.sounds = SoundManager()
        
    def update_score(self):
        """Call this whenever the bird successfully passes a pipe"""
        self.score += 1
        
        #Play sound everytime the bird passes a pipe
        self.sounds.play_point()
        
    def reset_score(self):
        """Call this when the game restarts"""
        if self.score > self.high_score:   #Checks if the current score is greater than the high score
            self.high_score = self.score   #Then sets the high score equal to the current score
        self.score = 0                     #Resets the current score to 0 for the next match
        
    def draw(self, screen):
        """Draws the score on the screen only if we are in-game"""
        if game_states.in_game and not game_states.fail:  #Checks if the user is in a game and the game has not crashed
            
            #Render the text
            score_surface = self.font.render(str(self.score), True, self.color)       #Converts raw integers into a white colored surface image and turns on Anti=aliasing (Since pygame cannot draw raw text directly)
            score_rect = score_surface.get_rect(center = (self.pos_x, self.pos_y))    #Centers the surface image (displayed score) at the specified position
            
            #Draw shadow for better visibility (optional visual flair)
            shadow_surface = self.font.render(str(self.score), True, (0, 0, 0))               #Create a duplicate surface image (displayed score) in black for shadow effect
            shadow_rect = score_surface.get_rect(center = (self.pos_x + 2, self.pos_y + 2))   #Offset the shadow by 2 pixels down and right
            
            screen.blit(shadow_surface, shadow_rect)  #Draw shadow first so it appears behind the main score
            screen.blit(score_surface, score_rect)    #Draw the main score second so it appears on top of the shadow image
            
        