import pygame
from particles import Particles

class Grenade(pygame.sprite.Sprite):
    def __init__(self, player_rect, group, looking_right, particle_sprites, enemy_collision, floor_collision):
        super().__init__(group)
        self.width = 4
        self.height = 4
        self.direction = pygame.math.Vector2(0,0)
        self.image = pygame.image.load("./assets/weapons/grenade.png")
        self.gravity = 0.8
        self.throw_strength = -12
        self.throw_length = 10
        self.thrown = False
        self.damage = 5
        self.looking_right = looking_right
        self.particle_sprites = particle_sprites
        self.enemy_collision = enemy_collision
        self.floor_collision = floor_collision
    
        # setup rect
        if self.looking_right:
            self.rect = self.image.get_rect(topleft = player_rect.topright)
        else:
            self.rect = self.image.get_rect(topright = player_rect.topleft)
        
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        self.rect.x += self.direction.x
    
    def throw(self):
        if self.looking_right:
            self.direction.y = self.throw_strength
            self.direction.x = self.throw_length
            self.thrown = False
        else:
            self.direction.y = self.throw_strength
            self.direction.x = -self.throw_length
            self.thrown = False
    
    
    def update(self, enemies, tiles):
        self.add_gravity()
        self.enemy_collision(self, enemies)
        self.floor_collision(self, tiles)
        
        