import pygame
import random

from Monster import Boss


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('Assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 10)
        self.rect.x = random.randint(400, 1600)
        self.rect.y = - random.randint(100, 800)  # Changé pour commencer au-dessus de l'écran
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('Comet')

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.start()
            self.comet_event.game.spawn_monster(Boss)

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 1080:  # Changé de 1100 à 1080
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            self.remove()
            self.comet_event.game.player.damage(30)