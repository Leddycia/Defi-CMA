import pygame

from player import Player
from Monster import Monster, Mummy, Alien, Boss
from comet_event import CometFallEvent
from sounds import SoundManager


class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        self.font = pygame.font.SysFont('Arial', 50, bold=True)  # Police système au cas où
        self.score = 0
        self.pressed = {}

    def add_score(self, points):
        self.score += points

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        self.spawn_monster(Alien)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('Game_Over')
        self.sound_manager.play('Song')

    def update(self, screen):

        # Dessiner d'abord tous les sprites
        screen.blit(self.player.image, self.player.rect)

        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)
        self.comet_event.all_comets.draw(screen)

        # Puis les barres de vie
        self.player.update_health_bar(screen)

        for monster in self.all_monsters:
            monster.update_health_bar(screen)

        # Puis la barre d'événement
        self.comet_event.update_bar(screen)

        # ENFIN le score EN DERNIER pour qu'il soit au-dessus de tout
        score_text = self.font.render(f'SCORE: {self.score}', True, (255, 255, 0))
        screen.blit(score_text, (1550, 30))

        # Update logic
        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1720:
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 100:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))