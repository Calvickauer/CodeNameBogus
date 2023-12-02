import pygame
from support import *

class Particles(pygame.sprite.Sprite):
    def __init__(self, position, particle_type):
        super().__init__()
        self.import_assests()
        self.frame_index = 0
        self.animation_speed = .15
        self.particle_type = particle_type
        self.image = pygame.Surface((20,20))
        self.image.fill("blue")
        self.rect = self.image.get_rect(center = position.center)
        
            
    def import_assests(self):
        path = "assets/particles/"
        self.animations = {"explosion": []}
        for animation in self.animations.keys():
            fullpath = path + animation
            self.animations[animation] = import_folder(fullpath)
    
    def update(self):
        pass