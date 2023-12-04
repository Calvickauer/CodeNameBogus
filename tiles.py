import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./assets/terrain/floor.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, shift):
        self.rect.x += shift
        
