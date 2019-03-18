from block import *
from pile import *

import numpy as np
from random import choice
from time import time
from pygame import draw

class Grid:
    def __init__(self, screen):
        self.grid = np.zeros((10,20))
        self.pile = np.zeros((10,20))
        self.screen = screen
        self.activeBlock = None
        self.lastFallTime = time()
        self.fallFreq = 1

    def update(self):
        if time() - self.lastFallTime > self.fallFreq:
            if self.activeBlock is not None:
                self.activeBlock.fall()
                self.lastFallTime = time()
            else: self.spawn()

    def show(self):
        for y_index, line in enumerate(self.grid.T):
            for x_index, pixl in enumerate(line):
                color = (0,0,0)
                if pixl == 1.0:
                    color = (255,255,0)
                if pixl == 2.0:
                    color = (0,255,255)
                if pixl == 3.0:
                    color = (128,0,128)
                if pixl == 4.0:
                    color = (0,255,50)
                if pixl == 5.0:#z
                    color = (0,255,50)
                if pixl == 6.0:#j
                    color = (0,0,255)
                if pixl == 7.0:#l
                    color = (0,255,128)
                if pixl == 8.0:
                    color = (255,255,255)
                #print(index,': ',pixl,': ',(x, y, 29, 29))
                draw.rect(self.screen, (255,255,255), (x_index*29, y_index*29, 29, 29),1)
                draw.rect(self.screen, color, (x_index*29+1, y_index*29+1, 27, 27))

    def reset(self):
        self.grid = np.zeros((10,20))
        self.grid += self.pile


    def spawn(self):
        block_type = choice("IOTSZJL")
        if block_type == "I":
            self.activeBlock = I()
        if block_type == "O":
            self.activeBlock = O()
        if block_type == "T":
            self.activeBlock = T()
        if block_type == "S":
            self.activeBlock = S()
        if block_type == "Z":
            self.activeBlock = Z()
        if block_type == "J":
            self.activeBlock = J()
        if block_type == "L":
            self.activeBlock = L()

    def fit_block(self):
        if self.activeBlock is not None:
            shape = self.activeBlock.array.shape
            x = self.activeBlock.x
            y = self.activeBlock.y

            self.grid[x:x+shape[1],y:y+shape[0]] += self.activeBlock.array.T

    def check(self, move):
        if self.activeBlock is not None:
            shape = self.activeBlock.array.shape
            x = self.activeBlock.x
            y = self.activeBlock.y

            if y + shape[0] > 19:
                self.pile[x:x+shape[1],y:y+shape[0]] += self.activeBlock.array.T
                self.activeBlock = None
                return

            if move == "down":
                next_x = x
                next_y = y+1
            if move == "left":
                next_x = x-1
                next_y = y
            if move == "right":
                next_x = x+1
                next_y = y

            section = self.pile[next_x:next_x+shape[1],next_y:next_y+shape[0]] * self.activeBlock.array.T

            for cell in np.nditer(section):
                if cell != 0:
                    if move == "left" or move == "right":
                        #self.activeBlock.doNotMove jak to zrobic...
                        return
                    if move == "down":
                        self.pile[x:x+shape[1],y:y+shape[0]] += self.activeBlock.array.T
                        self.activeBlock = None
                        return
