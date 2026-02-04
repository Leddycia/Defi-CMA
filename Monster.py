import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x = 1900 + random.randint(0, 500)
        self.rect.y = 800 - offset  # Sur le sable
        self.loot_amount = 10

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1900 + random.randint(0, 500)
            self.velocity = random.randint(2, 5)
            self.health = self.max_health
            self.game.add_score(self.loot_amount)

        if self.game.comet_event.is_full_loading():
            self.game.all_monsters.remove(self)
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 4])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 4])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, 'mummy', (128, 128))
        self.set_speed(7)
        self.set_loot_amount(20)


class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, 'alien', (128, 128))
        self.attack = 5
        self.set_speed(6)
        self.set_loot_amount(50)


class Boss(Monster):
    def __init__(self, game):
        super().__init__(game, 'Boss', (400, 400), 200)
        self.health = 450
        self.max_health = 450
        self.attack = 10
        self.set_speed(5)
        self.set_loot_amount(100)