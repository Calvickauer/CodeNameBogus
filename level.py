import pygame
from settings import *
from tiles import Tile
from player import Player


class Level: 
    def __init__(self, maps, screen):
        self.screen = screen
        
        self.setup_level(maps)
        
    def setup_level(self, map):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(map):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_W
                y = row_index * TILE_W
                if cell == "X":
                    tile = Tile((x,y), TILE_W)
                    self.tiles.add(tile)
                if cell == "P":
                    player_character = Player((0,0))
                    self.player.add(player_character)
    
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
                        
    
    def run(self): 
        self.tiles.update()
        self.tiles.draw(self.screen)
        self.player.update()
        self.vertical_collsion()
        self.horizontal_collison()
        self.player.draw(self.screen)
        
        