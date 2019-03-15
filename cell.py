import pygame

class Cell:

    def __init__(self, x, y, len_x, len_y, screen):
        self.rect = (x, y, len_x, len_y)
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.screen = screen
        self.base_color = (255,255,255,90)
        self.color = (255,255,255,90)
        self.piled = False

    def show(self):
        if self.color != self.base_color:
            width = 0
        else: width = 1
        pygame.draw.rect(self.screen, self.color, self.rect, width)