import pygame
from comet import Comet


class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 50
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loading(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 15):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loading() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):

        self.add_percent()

        # Barre en bas de l'écran
        bar_height = 20
        bar_y = surface.get_height() - bar_height - 5

        # Fond noir de la barre
        pygame.draw.rect(surface, (30, 30, 30), [
            0,
            bar_y,
            surface.get_width(),
            bar_height
        ])

        # Barre de progression rouge vif
        pygame.draw.rect(surface, (255, 0, 0), [
            0,
            bar_y,
            (surface.get_width() / 100) * self.percent,
            bar_height
        ])

        # Bordure blanche pour meilleure visibilité
        pygame.draw.rect(surface, (255, 255, 255), [
            0,
            bar_y,
            surface.get_width(),
            bar_height
        ], 2)