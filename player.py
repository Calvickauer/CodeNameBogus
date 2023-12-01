import pygame
from settings import *
from gun import Gun

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, bullets):
        super().__init__()
        self.image = pygame.Surface((62,62))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)
        self.bullets = bullets
        
        # stats
        
        self.health = 100
        
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
        if keys[pygame.K_c]:
            self.shoot()
    
    def shoot(self):
        bullet = Gun(self.rect.center, self.looking_right)
        self.bullets.add(bullet)
        
        
            
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y += -20

    
    def update(self):
        self.input()
    
