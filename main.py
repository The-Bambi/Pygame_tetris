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
            if event.key == pygame.K_RCTRL:
                grid.spawn()
            if event.key == pygame.K_LEFT:
                grid.activeBlock.moveLeft()
            if event.key == pygame.K_RIGHT:
                grid.activeBlock.moveRight()
            if event.key == pygame.K_DOWN:
                grid.activeBlock.fall()

    
    screen.fill((0,0,0))

    grid.update(pygame.time.get_ticks())
    grid.show()

    pygame.display.flip()
    clock.tick(30)