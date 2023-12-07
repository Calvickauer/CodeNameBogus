import pygame

class Shotgun(pygame.sprite.Sprite):

    def __init__(self, player, group, direction, enemies, spread):
        super().__init__(group)
        self.width = 7
        self.height = 7
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("darkblue")
        if player.looking_right:
            self.rect = self.image.get_rect(topleft = (player.rect.x + 67, player.rect.y + 28))
        else:
            self.rect = self.image.get_rect(topleft = (player.rect.x, player.rect.y + 28))
        self.speed = 20
        self.direction = direction
        self.enemies = enemies
        self.spread = spread
        self.shooter = player.rect

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

    def update(self, var, var1):
        self.orientation()
        self.collision()
        self.spread_distance()
    