import pygame
from settings import *
from gun import Gun
from grenade import Grenade

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, bullets, enemies, grenades, particle_sprites):
        super().__init__()
        self.image = pygame.Surface((62,62))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)
        self.bullets = bullets
        self.enemies = enemies
        self.grenades = grenades
        self.particle_sprites = particle_sprites
        
        # stats
        
        self.health = 100
        
        # cool downs
        
        self.gun_cooldown = .5
        self.gun_cooldown_time = 0
        self.grenade_cooldown = 1
        self.grenade_cooldown_time = 0
                        
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
        if keys[pygame.K_z]:
            current_time = pygame.time.get_ticks()
            if current_time - self.grenade_cooldown_time > self.grenade_cooldown * 1000:
                grenade = Grenade(self.rect, self.looking_right, self.particle_sprites)
                self.grenades.add(grenade)
                grenade.throw()
                self.grenade_cooldown_time = current_time
    
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.gun_cooldown_time > self.gun_cooldown * 1000:
            bullet = Gun(self.rect.center, self.looking_right,self.enemies)
            self.bullets.add(bullet)
            self.gun_cooldown_time = current_time
        
        
            
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y += -20

    
    def update(self):
        self.input()
    
