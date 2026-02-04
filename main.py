import math
import pygame
from game import Game

pygame.init()
clock = pygame.time.Clock()
FPS = 120
pygame.display.set_caption('Defi CMA')
screen = pygame.display.set_mode((1920, 1080))

# Charger les images avec leurs dimensions originales
background = pygame.image.load('Assets/bg4.jpg')
banner = pygame.image.load('Assets/BY.png')
play_button = pygame.image.load('Assets/But.png')

# Redimensionner le background pour couvrir l'écran tout en permettant le défilement
background = pygame.transform.scale(background, (2500, 1080))
bg_width = 2500

# Centre de l'écran
center_x = screen.get_width() // 2
center_y = screen.get_height() // 2

# Bannière plus grande, centrée
banner = pygame.transform.scale(banner, (400, 327))
banner_rect = banner.get_rect()
banner_rect.centerx = center_x
banner_rect.centery = center_y - 150

# Bouton play juste en dessous de la bannière, centré
play_button = pygame.transform.scale(play_button, (200, 200))
play_button_rect = play_button.get_rect()
play_button_rect.centerx = center_x
play_button_rect.top = banner_rect.bottom + 30

game = Game()
x_background = 0
running = True
game.sound_manager.play('Song')

while running:
    # Défilement horizontal du background
    x_background -= 1

    # Repositionner quand le défilement atteint la fin
    if x_background <= -(bg_width - 1920):
        x_background = 0

    # Toujours afficher le background en premier
    screen.blit(background, (x_background, 0))

    if game.is_playing:
        # Le jeu dessine tout par-dessus le background
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_w:
                game.player.launch_Projectile()
            if event.key == pygame.K_SPACE:
                game.start()
                game.sound_manager.play('click')
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play('click')

    clock.tick(FPS)