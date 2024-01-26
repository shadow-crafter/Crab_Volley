import os, pygame

DEFAULT_IMG_PATH = 'assets/images/'

def load_image(path: str) -> pygame.Surface:
    img = pygame.image.load(DEFAULT_IMG_PATH + path).convert()
    img.set_colorkey((255, 255, 255))
    return img
