from cell import *
from block import *
from pile import *

import numpy as np

from random import choice
from time import time

class Grid:
    def __init__(self, x_amount, y_amount, screen):
        self.grid = np.zeros((20,10))
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


