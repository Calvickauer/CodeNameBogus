import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((62,62))
        self.image.fill("red")
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
        
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.looking_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.looking_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
            
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y += -20
    
    def update(self):
        self.input()
