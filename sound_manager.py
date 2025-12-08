import pygame

class SoundManager:
    def __init__(self):
        
        #Initializes audio mixer only once
        if not pygame.mixer.get_init():  #Checks to see that the audio mixer isn't turned on
            pygame.mixer.init()          #Then it turns the audio mixer on
        
        
        #Load sounds once to save memory
        try:
            #Reads the sound file and converts it into audible sound
            self.sound_point = pygame.mixer.Sound(r"assets\audio\sfx_point.mp3")  #r tells the system to treat the string exactly as written
        
        #Throws an exception if any error happens in the try block
        except Exception as e:
            print(f"Sound file is missing. {e}")
            self.sound_point = None
            
    
    def play_point(self):
        if self.sound_point:         #Checks if we actually have a valid sound file loaded (fails even if set to None)
            self.sound_point.play()  #If true then plays the corresponding sound to speakers once
            