import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(125, 125)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load('Assets/' + sprite_name + '.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)

    def animate(self):
        self.current_image += 1

        if self.current_image >= len(self.images):
            self.current_image = 0

        self.image = self.images[self.current_image]

        self.image = pygame.transform.scale(self.image, self.size)


def load_animation_images(sprite_name):
    images = []
    path = f'Assets/{sprite_name}/{sprite_name}'
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images


animations = {
    'mummy': load_animation_images('mummy'),
    'alien': load_animation_images('alien'),
    'Boss': load_animation_images('Boss')
}
