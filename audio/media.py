import pygame
import sys

pygame.init()

class Media_player:
    def __init__(self,sound:str):
        pygame.mixer.init()
        self.sound= sound

    def load_sound(self):
        pygame.mixer.music.load(self.sound)

    def play(self):
        pygame.mixer.music.play()

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    def mute(self):
        pass