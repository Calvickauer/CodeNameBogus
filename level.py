import pygame
from settings import *
from tiles import Tile
from player import Player
from gun import Gun
from enemy import Enemy


class Level: 
    def __init__(self, maps, screen):
        self.screen = screen
        self.shift = 0
        self.setup_level(maps)
        self.dead = False
        self.gun = Gun
    
    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < SCROLL_T and direction_x < 0:
            self.shift = SHIFT_AMOUNT
            player.speed = 0
        elif player_x > SCREEN_WIDTH - SCROLL_T and direction_x > 0:
            self.shift = -SHIFT_AMOUNT
            player.speed = 0
        else:
            self.shift = 0
            player.speed = 8
        
    
    
    def setup_level(self, map):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.grenades = pygame.sprite.Group()
        self.particle_sprites = pygame.sprite.Group()
        
        for row_index, row in enumerate(map):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_W
                y = row_index * TILE_W
                if cell == "X":
                    print(x, y)
                    tile = Tile((x,y), TILE_W)
                    self.tiles.add(tile)
                if cell == "P":
                    player_character = Player((0,0), self.bullets, self.enemies, self.grenades, self.particle_sprites)
                    self.player.add(player_character)
                if cell == "E":
                    enemy_character = Enemy((x,y))
                    self.enemies.add(enemy_character)
    
    def vertical_collsion(self):
        player = self.player.sprite
        player.add_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                    
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False
                
    def enemy_vertical_collsion(self):
        for enemy in self.enemies.sprites():
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.y > 0:
                        enemy.rect.bottom = sprite.rect.top
                        enemy.direction.y = 0
                        enemy.on_ground = True
                    elif enemy.direction.y < 0:
                        enemy.rect.top = sprite.rect.bottom
                        enemy.direction.y = 0
                        enemy.on_ceiling = True
                    
            if enemy.on_ground and enemy.direction.y < 0 or enemy.direction.y > 1:
                enemy.on_ground = False
            
            if enemy.on_ceiling and enemy.direction.y > 0:
                enemy.on_ceiling = False
                
    def horizontal_collison(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True

        if player.on_left and player.direction.x >= 0:
            player.on_left = False
        if player.on_right and player.direction.x <= 0:
            player.on_roght = False
    
    def enemy_horizontal_collison(self):
        for enemy in self.enemies.sprites():
            enemy.rect.x += enemy.direction.x * enemy.speed
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                        enemy.on_left = True
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left
                        enemy.on_right = True

        if enemy.on_left and enemy.direction.x >= 0:
            enemy.on_left = False
        if enemy.on_right and enemy.direction.x <= 0:
            enemy.on_roght = False
        
        
    def death(self):
        player = self.player.sprite
        if player.health <= 0:
            self.dead = True
        if player.rect.y > SCREEN_HEIGHT:
            player.health = 0
    
    def run(self): 
        self.tiles.update(self.shift)
        self.tiles.draw(self.screen)
        self.scroll()
        self.player.update()
        self.vertical_collsion()
        self.horizontal_collison()
        self.player.draw(self.screen)
        self.death()
        self.grenades.update(self.enemies)
        self.grenades.draw(self.screen)
        self.bullets.update()
        self.bullets.draw(self.screen)
        self.enemies.update(self.shift)
        self.enemies.draw(self.screen)
        self.enemy_vertical_collsion()
        self.enemy_horizontal_collison()
        self.particle_sprites.update()
        self.particle_sprites.draw(self.screen)
        
        