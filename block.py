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
        self.array = shape

    def fall(self):
        self.y +=1

    def moveLeft(self):
        if self.x == 0:
            return
        self.x -= 1

    def moveRight(self):
        if self.x == 10 - self.array.shape[1]:
            return
        self.x += 1

    def rotate(self):
        if (self.array.shape[0] + self.x) > 9:
            self.x -= 1
        if (self.array.shape[1] + self.y) > 19:
            self.y -=1
        self.array = np.rot90(self.array)


class O(Block):

    def __init__(self):
        super().__init__(4, np.array([[1,1],[1,1]]))

class I(Block):

    def __init__(self):
        super().__init__(3, np.array([[2,2,2,2]]))

class T(Block):

    def __init__(self):
        super().__init__(4, np.array([[0,3,0],[3,3,3],[0,0,0]]))

class S(Block):

    def __init__(self):
        super().__init__(4, np.array([[0,4,4],[4,4,0],[0,0,0]]))

class Z(Block):

    def __init__(self):
        super().__init__(4, np.array([[5,5,0],[0,5,5],[0,0,0]]))

class J(Block):

    def __init__(self):
        super().__init__(4, np.array([[6,0,0],[6,6,6],[0,0,0]]))

class L(Block):

    def __init__(self):
        super().__init__(4, np.array([[0,0,7],[7,7,7],[0,0,0]]))

class test(Block):

    def __init__(self):
        super().__init__(5, np.array([[8]]))
