import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.width = 62
        self.height = 62
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("darkgreen")
        self.rect = self.image.get_rect(topleft = pos)
        
        # movement
        
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.speed = 8
        self.looking_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
    
    
    def add_gravity(self):
        if not self.on_ground:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y
        else:
            pass
        
    def update(self, shift):
        self.rect.x += shift
        self.add_gravity()
    