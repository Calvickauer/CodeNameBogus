import pygame
from particles import Particles

class Grenade(pygame.sprite.Sprite):
    def __init__(self, player_rect, looking_right, particle_sprites):
        super().__init__()
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
    
        # setup rect
        if self.looking_right:
            self.rect = self.image.get_rect(topleft = player_rect.topright)
        else:
            self.rect = self.image.get_rect(topright = player_rect.topleft)
        
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        self.rect.x += self.direction.x
    
    def enemy_collision(self,enemies):
        enemies_hit = pygame.sprite.spritecollide(self, enemies, False)
        if enemies_hit:
            effects = Particles(self.rect, "explosion")
            self.particle_sprites.add(effects)
            for enemey in enemies_hit:
                self.kill()
                
    def floor_collision(self, tiles):
        floor_hit = pygame.sprite.spritecollide(self, tiles, False)
        if floor_hit:
            effects = Particles(self.rect, "explosion")
            self.particle_sprites.add(effects)
            for tile in floor_hit:
                self.kill()
    
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
        self.enemy_collision(enemies)
        self.floor_collision(tiles)
        
        