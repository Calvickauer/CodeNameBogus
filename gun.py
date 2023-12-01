import pygame

class Gun(pygame.sprite.Sprite):

    def __init__(self, pos, direction):
        super().__init__()
        self.width = 5
        self.height = 2
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("orange")
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 20
        self.direction = direction
    
    def orientation(self):
        if self.direction:
            self.rect.x += self.speed  
        else:
            self.rect.x -= self.speed

    def update(self):
        self.orientation()
    