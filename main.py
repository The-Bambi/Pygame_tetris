import pygame
from grid import *

pygame.init()

screen = pygame.display.set_mode((400, 581))
clock = pygame.time.Clock()
grid = Grid(10, 20, screen)

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                done = True

    
    screen.fill((0,0,0))

    grid.grid[5][3].up.color = (255,0,0)
    grid.grid[5][3].down.color = (255,0,0)
    grid.grid[5][3].right.color = (255,0,0)
    grid.grid[5][3].left.color = (255,0,0)
    grid.show()

    pygame.display.flip()
    clock.tick(120)