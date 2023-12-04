import pygame
from settings import *
from gun import Gun
from grenade import Grenade
from support import *
from shotgun import Shotgun

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, bullets, enemies, grenades, particle_sprites):
        super().__init__()
        self.import_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        # self.image = pygame.Surface((62,62))
        # self.image.fill("red")
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.bullets = bullets
        self.enemies = enemies
        self.grenades = grenades
        self.particle_sprites = particle_sprites
        self.primary_weapons = PRIMARY_WEAPONS['handgun']
        self.secondary_weapons = SECONDARY_WEAPONS['shotgun']
        self.heavy_weapons = HEAVY_WEAPONS['machinegun']
        self.equipped_weapon = self.secondary_weapons        
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
        self.status = "idle"
        
    def import_assets(self):
        path = "assets/player/"
        self.animations = {"fall": [],"idle": [],"jump": [],"run": [],"shoot": []}
        for animation in self.animations.keys():
            fullpath = path + animation
            print(fullpath)
            self.animations[animation] = import_folder(fullpath)
    
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
            if self.equipped_weapon["name"] == "handgun":
                bullet = Gun(self.rect.center, self.looking_right,self.enemies)
                self.bullets.add(bullet)
                self.gun_cooldown_time = current_time
            elif self.equipped_weapon['name'] == 'shotgun':
                bullet = Shotgun(self.rect, self.looking_right,self.enemies, -2)
                bullet1 = Shotgun(self.rect, self.looking_right,self.enemies, -1)
                bullet2 = Shotgun(self.rect, self.looking_right,self.enemies, 0)
                bullet3 = Shotgun(self.rect, self.looking_right,self.enemies, 1)
                bullet4 = Shotgun(self.rect, self.looking_right,self.enemies, 2)
                self.bullets.add(bullet, bullet1, bullet2, bullet3, bullet4)
                self.gun_cooldown_time = current_time
                
            
        
        
            
    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y += -20
    
    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        if self.looking_right:
            self.image = image
        else:
            flip_image = pygame.transform.flip(image, True, False)
            self.image = flip_image
        # setup the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
    
    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"
                
            
    def update(self):
        self.input()
        self.animate()
        self.get_status()
    
