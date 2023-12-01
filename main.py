import pygame, sys
from settings import *
from level import Level
from tiles import Tile
from game_over import GameOver

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level = Level(MAPS["map_one"], screen)
game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT,"Game Over", 36, (255, 255, 255))


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    
    if not level.dead:
        level.run()
    elif level.dead:
        game_over.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        level.dead = False
        level = Level(MAPS["map_one"], screen)
    pygame.display.update()
    
    
    clock.tick(60)
    



