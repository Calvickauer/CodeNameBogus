import pygame
from support import *

class Particles(pygame.sprite.Sprite):
    def __init__(self, position, particle_type):
        super().__init__()
        self.import_assets()
        self.frame_index = 0
        self.animation_speed = .15
        self.particle_type = particle_type
        self.image = pygame.Surface((20,20))
        self.image.fill("blue")
        self.position = position
        
        
            
    def import_assets(self):
        path = "assets/particles/"
        self.animations = {"explosion": []}
        for animation in self.animations.keys():
            fullpath = path + animation
            self.animations[animation] = import_folder(fullpath)
    
    def animate(self):
        animation = self.animations["explosion"]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            self.kill()
        image = animation[int(self.frame_index)]
        self.image = image
        self.rect = self.image.get_rect(center = self.position.center)
    
    def update(self):
        self.animate()