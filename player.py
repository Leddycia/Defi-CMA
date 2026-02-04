import pygame
from Projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 250
        self.max_health = 250
        self.attack = 15
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('Assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 800  # Sur le sable (entre 650 et 880)

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 60, self.rect.y - 20, self.max_health, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 60, self.rect.y - 20, self.health, 8])

    def launch_Projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.play('Tir')

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity