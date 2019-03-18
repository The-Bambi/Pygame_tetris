import pygame
from grid import *

pygame.init()

screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
grid = Grid(screen)

done = False
grid.show()
grid.spawn()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                done = True
            if grid.activeBlock is not None:
                if event.key == pygame.K_RCTRL:
                    grid.spawn()
                if event.key == pygame.K_LEFT:
                    grid.activeBlock.moveLeft()
                if event.key == pygame.K_RIGHT:
                    grid.activeBlock.moveRight()
                if event.key == pygame.K_DOWN:
                    grid.activeBlock.fall()
                if event.key == pygame.K_UP:
                    grid.activeBlock.rotate()

    screen.fill((0,0,0))

    grid.fit_block()
    grid.update()
    grid.check()
    grid.show()
    grid.reset()

    pygame.display.flip()
    clock.tick(30)