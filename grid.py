from cell import *
from block import *
from random import choice

class Grid:
    
    def __init__(self, x_amount, y_amount, screen):
        self.grid = [[Cell(x*29, y*29, 30, 30, screen) for x in range(x_amount)] for y in range(y_amount)]
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                if y > 0:
                    cell.up = self.grid[y-1][x]
                if y < y_amount - 1:
                    cell.down = self.grid[y+1][x]
                if x > 0:
                    cell.left = self.grid[y][x-1]
                if x < x_amount - 1:
                    cell.right = self.grid[y][x+1]
        self.activeBlock = None

    def show(self):
        for line in self.grid:
            for cell in line:
                cell.show()

    def update(self, frameCount):
        if frameCount%60 == 0:
            if self.activeBlock is not None and self.activeBlock.active:
                self.activeBlock.fall()

    def spawn(self):
        print("spawned")
        #block_type = choice("IOTSZJL")
        block_type = "O"
        if block_type == "O":
            anchor = self.grid[0][4]
            self.activeBlock = Block("O", anchor)
        if block_type == ".":
            anchor = self.grid[0][4]
            self.activeBlock = Block(".", anchor)


