import pygame
from settings import *
from tiles import Tile
from player import Player
from gun import Gun
from enemy import Enemy
from support import *
from shotgun import *
from grenade import Grenade
from particles import Particles

class Level: 
    def __init__(self, maps, screen):
        self.screen = screen
        self.setup_level(maps)
        self.dead = False
        self.gun = Gun
        
    
    # def scroll(self):
    #     player = self.player.sprite
    #     player_x = player.rect.centerx
    #     direction_x = player.direction.x
        
    #     if player_x < SCROLL_T and direction_x < 0:
    #         self.shift = SHIFT_AMOUNT
    #         player.speed = 0
    #     elif player_x > SCREEN_WIDTH - SCROLL_T and direction_x > 0:
    #         self.shift = -SHIFT_AMOUNT
    #         player.speed = 0
    #     else:
    #         self.shift = 0
    #         player.speed = 8
        
    
    
    def setup_level(self, map):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.grenades = pygame.sprite.Group()
        self.particle_sprites = pygame.sprite.Group()
        self.visible_sprites = YSortCameraGroup()
        
        layouts = {
            "floor": import_csv_layout("./assets/map2/level2_floor.csv"),
            "enemy": import_csv_layout("./assets/map2/level2_enemy.csv"),
            "boundary": import_csv_layout("./assets/map2/level2_boundaries.csv"),
            "level_one": import_csv_layout('./assets/map2/level2_level.csv')
        }
        player_character = Player(
            (75,404),
            [self.visible_sprites, self.player],
            self.shoot,
            self.throw_grenade)
        
        for style,layout in layouts.items():
        
            for row_index, row in enumerate(layout):
                for col_index, cell in enumerate(row):
                    x = col_index * TILE_W
                    y = row_index * TILE_W
                    if cell != "-1":
                        if style == "floor" or style == "boundary":
                            tile = Tile((x,y),[self.visible_sprites], TILE_W)
                            self.tiles.add(tile)
                        if style == "enemy":
                            enemy_character = Enemy((x,(y - 60)), [self.visible_sprites, self.enemies])
                        if style == "level_one":
                            print("particles")
                            Particles((x,(y - 128)),[self.particle_sprites, self.visible_sprites], style)
                            
                            
            
    
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
            enemy.on_right = False
        
        
    def death(self):
        player = self.player.sprite
        if player.health <= 0:
            self.dead = True
        if player.rect.y > SCREEN_HEIGHT:
            player.health = 0
    
    # PLAYER ACTIONS 
    
    def shoot(self, shooter):
        player = self.player.sprite
        if player.equipped_weapon["name"] == "machinegun":
            bullet = Gun(player, [self.visible_sprites, self.bullets], player.looking_right, self.enemies, shooter)
        current_time = pygame.time.get_ticks()
        if current_time - player.gun_cooldown_time > player.gun_cooldown * 1000:
            if player.equipped_weapon["name"] == "handgun":
                bullet = Gun(player, [self.visible_sprites, self.bullets], player.looking_right, self.enemies, shooter)
                player.gun_cooldown_time = current_time
            elif player.equipped_weapon['name'] == 'shotgun':
                bullet = Shotgun(player,[self.visible_sprites, self.bullets], player.looking_right,self.enemies, -2)
                bullet1 = Shotgun(player,[self.visible_sprites, self.bullets], player.looking_right,self.enemies, -1)
                bullet2 = Shotgun(player,[self.visible_sprites, self.bullets], player.looking_right,self.enemies, 0)
                bullet3 = Shotgun(player,[self.visible_sprites, self.bullets], player.looking_right,self.enemies, 1)
                bullet4 = Shotgun(player,[self.visible_sprites, self.bullets], player.looking_right,self.enemies, 2)
                player.gun_cooldown_time = current_time
            
    
    def throw_grenade(self):
        player = self.player.sprite
        current_time = pygame.time.get_ticks()
        if current_time - player.grenade_cooldown_time > player.grenade_cooldown * 1000:
            grenade = Grenade(player.rect,[self.visible_sprites, self.grenades], player.looking_right, self.particle_sprites, self.enemy_collision, self.floor_collision)
            grenade.throw()
            player.grenade_cooldown_time = current_time  
                
    # ------------------------------------------------------------------------
    
    # particle actions
    
    # grenade actions
    
    def enemy_collision(self, grenade, enemies):
        enemies_hit = pygame.sprite.spritecollide(grenade, enemies, False)
        if enemies_hit:
            effects = Particles((grenade.rect.x, (grenade.rect.y - 128)), [self.visible_sprites], "explosion")
            grenade.particle_sprites.add(effects)
            for enemey in enemies_hit:
                grenade.kill()
                
    def floor_collision(self, grenade, tiles):
        floor_hit = pygame.sprite.spritecollide(grenade, tiles, False)
        if floor_hit:
            effects = Particles((grenade.rect.x, (grenade.rect.y - 128)), [self.visible_sprites], "explosion")
            grenade.particle_sprites.add(effects)
            for tile in floor_hit:
                grenade.kill()
    # ------------------------------------------
    
    def run(self): 
        player = self.player.sprite
        self.visible_sprites.custom_draw(player)
        self.visible_sprites.update(self.enemies, self.tiles)
        # self.tiles.update()
        # self.tiles.draw(self.screen)
        # self.scroll()
        # self.player.update()
        self.vertical_collsion()
        self.horizontal_collison()
        # self.player.draw(self.screen)
        # self.death()
        # self.grenades.update(self.enemies, self.tiles)
        # self.grenades.draw(self.screen)
        # self.bullets.update()
        # self.bullets.draw(self.screen)
        # self.enemies.update(self.shift)
        # self.enemies.draw(self.screen)
        self.enemy_vertical_collsion()
        self.enemy_horizontal_collison()
    
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #CREATE FLOOR
        self.floor_surf = pygame.image.load('./assets/map2/map2.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):

        # offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw floor
        floor_upset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_upset_pos)


        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)