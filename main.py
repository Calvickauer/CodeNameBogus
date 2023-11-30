import pygame, sys
from settings import *
from level import Level
from tiles import Tile
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level = Level(MAPS["map_one"], screen)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    level.run()
    pygame.display.update()
    
    
    clock.tick(60)
    



