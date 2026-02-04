import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound('Assets/S#/click.ogg'),
            'Game_Over': pygame.mixer.Sound('Assets/S#/game_over.ogg'),
            'Comet': pygame.mixer.Sound('Assets/S#/meteorite.ogg'),
            'Tir': pygame.mixer.Sound('Assets/S#/tir.ogg'),
            'Song': pygame.mixer.Sound('Assets/S#/2.mp3')
        }

    def play(self, name):
        self.sounds[name].play()