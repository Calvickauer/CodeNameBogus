import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.width = 62
        self.height = 62
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("darkgreen")
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, shift):
        self.rect.x += shift
        