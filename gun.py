import pygame
import math 

class Gun(pygame.sprite.Sprite):

    def __init__(self, player_sprite, group, direction, enemies, shooter):
        super().__init__(group)
        self.width = 5
        self.height = 2
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("black")
        player = player_sprite
        if player.looking_right:
            self.rect = self.image.get_rect(topleft = (player.rect.x + 67, player.rect.y + 28))
        else:
            self.rect = self.image.get_rect(topleft = (player.rect.x, player.rect.y + 28))
        self.speed = 20
        self.direction = direction
        self.enemies = enemies
        self.shooter = shooter
    
    def collision(self):
        hit = pygame.sprite.spritecollide(self,self.enemies,False)
        if hit: 
            
            self.kill()
    
    def on_target(self, target_rect):
        # Calculate the direction vector towards the target
        direction = pygame.math.Vector2(target_rect.center) - pygame.math.Vector2(self.rect.center)
        direction.normalize()

        # Update the bullet's position based on the direction vector
        self.rect.x += self.speed * direction.x
        self.rect.y += self.speed * direction.y

        # Check for collisions or if the bullet goes off-screen
        self.enemy_collisions()
        self.check_offscreen()
        self.player_collision()

    def seek(self):
        if self.target:
            # Calculate the vector from the bullet to the target
            dx = self.target.rect.centerx - self.rect.centerx
            dy = self.target.rect.centery - self.rect.centery

            # Normalize the vector
            length = math.sqrt(dx **  2 + dy ** 2)
            if length != 0:
                dx /= length
                dy /= length

            # Update the direction of the bullet
            self.direction = pygame.math.Vector2(dx, dy)
        
    
    def orientation(self):
        if self.direction:
            self.rect.x += self.speed  
        else:
            self.rect.x -= self.speed

    def update(self, var, var1):
        self.orientation()
        self.collision()
    