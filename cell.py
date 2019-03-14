import pygame

class Cell:

    def __init__(self, x, y, len_x, len_y, screen):
        self.rect = (x, y, len_x, len_y)
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.screen = screen
        self.color = (255,255,255,90)
        self.width = 1

    def show(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.width)