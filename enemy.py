import pygame
from support import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.width = 62
        self.height = 62
        # self.image = pygame.Surface((self.width, self.height))
        # self.image.fill("darkgreen")
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        # movement
        
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.speed = 8
        self.status = "idle"
        self.looking_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
    
    def import_assets(self):
        path = "assets/enemy/"
        self.animations = {"exposion": [],"fall": [],"idle": [],"jump": [],"run": [],"shoot": []}
        for animation in self.animations.keys():
            fullpath = path + animation
            self.animations[animation] = import_folder(fullpath)
    
    
    def add_gravity(self):
        if not self.on_ground:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y
        else:
            pass
    
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
        
    def update(self, var, var1):
        self.add_gravity()
        self.get_status()
        self.animate()
    