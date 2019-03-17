from block import *
from pile import *

import numpy as np
from random import choice
from time import time
from pygame import draw

class Grid:
    def __init__(self, screen):
        self.grid = np.zeros((10,20))
        print(self.grid.shape)
        self.screen = screen
        self.activeBlock = None
        self.pile = Pile()
        self.lastFallTime = time()
        self.fallFreq = 1

    def update(self):
        if self.activeBlock is not None:
            if time() - self.lastFallTime > self.fallFreq:
                self.activeBlock.fall()
                    #self.pile.add_block(self.activeBlock)
                    #self.spawn()
                self.lastFallTime = time()

    def show(self):
        for y_index, line in enumerate(self.grid.T):
            for x_index, pixl in enumerate(line):
                color = (0,0,0)
                if pixl == 1.0:
                    color = (255,255,0)
                if pixl == 8:
                    color = (255,255,255)
                #print(index,': ',pixl,': ',(x, y, 29, 29))
                draw.rect(self.screen, (255,255,255), (x_index*29, y_index*29, 29, 29),1)
                draw.rect(self.screen, color, (x_index*29+1, y_index*29+1, 27, 27))

    def reset(self):
        self.grid = np.zeros((10,20))


    def spawn(self):
        '''
        if self.activeBlock is None:
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
        '''
        self.activeBlock = O()

    def fit_block(self):
        if self.activeBlock is not None:
            shape = self.activeBlock.array.shape
            x = self.activeBlock.x
            y = self.activeBlock.y

            self.grid[x:x+shape[0],y:y+shape[1]] = self.activeBlock.array

