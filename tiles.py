import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group, size):
        super().__init__(group)
        alpha_value = 0
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image.fill((1, 255, 255, alpha_value))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, var, var1):
        # self.rect.x += shift
        pass
        
