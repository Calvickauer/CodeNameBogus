import pygame

class Shotgun(pygame.sprite.Sprite):

    def __init__(self, pos, direction, enemies, spread):
        super().__init__()
        self.width = 7
        self.height = 7
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("lightblue")
        self.rect = self.image.get_rect(topleft = pos.center)
        self.speed = 20
        self.direction = direction
        self.enemies = enemies
        self.spread = spread
        self.shooter = pos

    def collision(self):
        hit = pygame.sprite.spritecollide(self,self.enemies,False)
        if hit: 
            self.kill()
    
    def spread_distance(self):
        start_position = self.shooter.x
        if self.direction:
            if self.rect.x >= (start_position + 300):
                self.kill()
            else:
                if self.rect.x < (start_position - 300):
                    self.kill()
                
    def orientation(self):
        if self.direction:
            self.rect.x += self.speed  
            self.rect.y += self.spread
        else:
            self.rect.x -= self.speed
            self.rect.y += self.spread

    def update(self):
        self.orientation()
        self.collision()
        self.spread_distance()
    