from cell import *
from block import *
from pile import *
from random import choice
from time import time

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
        self.pile = Pile()
        self.lastFallTime = time()
        self.fallFreq = 1

    def show(self):
        for line in self.grid:
            for cell in line:
                cell.show()

    def update(self, frameCount):
        if time() - self.lastFallTime > self.fallFreq:
            if self.activeBlock is not None:
                if not self.activeBlock.fall():
                    self.pile.add_block(self.activeBlock)
                    self.spawn()
                self.lastFallTime = time()

    def spawn(self):
        block_type = choice("IOTSZJL")
        if block_type == "I":
            self.activeBlock = I(self.grid[0][5])
        if block_type == "O":
            self.activeBlock = O(self.grid[0][4])
        if block_type == "T":
            self.activeBlock = T(self.grid[0][4])
        if block_type == "S":
            self.activeBlock = S(self.grid[0][4])
        if block_type == "Z":
            self.activeBlock = Z(self.grid[0][4])
        if block_type == "J":
            self.activeBlock = J(self.grid[0][4])
        if block_type == "L":
            self.activeBlock = L(self.grid[0][4])


