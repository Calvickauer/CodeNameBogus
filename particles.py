import pygame
from support import *

class Particles(pygame.sprite.Sprite):
    def __init__(self, position,group, particle_type):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.animation_speed = .15
        self.particle_type = particle_type
        self.image = self.animations[self.particle_type][self.frame_index]
        self.rect = self.image.get_rect(topleft = position)
            
    def import_assets(self):
        path = "assets/particles/"
        self.animations = {"explosion": [], "level_one": []}
        for animation in self.animations.keys():
            fullpath = path + animation
            self.animations[animation] = import_folder(fullpath)
    
    def animate(self):
        animation = self.animations[self.particle_type]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            if self.particle_type == 'explosion':
                self.kill()
        image = animation[int(self.frame_index)]
        self.image = image
        self.rect = self.image.get_rect(center = self.rect.center)
    
    def update(self, var, var1):
        self.animate()