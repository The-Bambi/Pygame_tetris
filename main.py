import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                done = True

    

    screen.fill((0,0,0))

    pygame.display.flip()
    clock.tick(120)