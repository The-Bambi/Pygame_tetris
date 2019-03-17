import numpy as np

'''
Cyan I
Yellow O
Purple T
Green S
Red Z
Blue J
Orange L
'''

class Block:
    def __init__(self, x, shape = np.array([1])):
        self.y = 0
        self.x = x
        self.shape = shape

    def fall(self):
        #print(self.cells[0].rect)
        self.y += 1

    def moveLeft(self):
        if self.x == 0:
            return
        self.x -= 1

    def moveRight(self):
        if self.x == 19:
            return
        self.x += 1

    def rotate(self):
        self.shape = np.rot90(self.shape)


class O(Block):

    def __init__(self):
        super().__init__(4, np.array([[[155,155,0],[155,155,0]],[[155,155,0],[155,155,0]]]))

class I(Block):

    def __init__(self):
        super().__init__(3, np.array([[[0,155,155],[0,155,155],[0,155,155],[0,155,155]]]))

class T(Block):

    def __init__(self):
        super().__init__(4, np.array([[[0,0,0],[155,0,155],[0,0,0]],[[155,0,155],[155,0,155],[155,0,155]]]))

class S(Block):

    def __init__(self):
        super().__init__(4, np.array([[[0,0,0],[0,155,0],[0,155,0]],[[0,155,0],[0,155,0],[0,0,0]]]))

class Z(Block):

    def __init__(self):
        super().__init__(4, np.array([[[155,0,0],[155,0,0],[0,0,0]],[[0,0,0],[155,0,0],[155,0,0]]]))

class J(Block):

    def __init__(self):
        super().__init__(4, np.array([[[0,0,155],[0,0,0],[0,0,0]],[[0,0,155],[0,0,155],[0,0,155]]]))

class L(Block):

    def __init__(self):
        super().__init__(4, np.array([[[0,0,0],[0,0,0],[205,155,0]],[[205,155,0],[205,155,0],[205,155,0]]]))
