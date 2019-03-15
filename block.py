'''
Cyan I
Yellow O
Purple T
Green S
Red Z
Blue J
Orange L
'''
I = [[1],[1],[1],[1]]
O = [[1,1],[1,1]]
T = [[0,1,0],[1,1,1]]
S = [[1,0],[1,1],[0,1]]
Z = [[0,1],[1,1],[1,0]]
J = [[0,1],[0,1],[1,1]]
L = [[1,0],[1,0],[1,1]]

from copy import deepcopy

class Block:
    def __init__(self, type, anchor):
        self.cells = []
        self.next_update = []
        self.color = None

        if type == ".":
            self.test = anchor
            self.color = (255,255,255)
            self.test.color = self.color
        if type == "O":
            self.color = (255,255,0)
            self.cells.append(anchor)
            self.cells.append(anchor.right)
            self.cells.append(anchor.right.down)
            self.cells.append(anchor.right.down.left)
            for cell in self.cells:
                cell.color = self.color
        if type == "I":
            self.cells.append(anchor)
            self.cells.append(anchor.right)
            self.cells.append(anchor.right.down)
            self.cells.append(anchor.right.down.left)

    def _fall(self):
        print(self.test.rect)
        self.test.color = self.test.base_color
        self.test = self.test.down
        self.test.color = (255,255,255)

    def fall(self):
        #print(self.cells[0].rect)
        for cell in self.cells:
            if cell.down is None or cell.down.piled:
                return False
        for cell in self.cells:
            cell.color = cell.base_color
        for cell in self.cells:
            next_cell = cell.down
            next_cell.color = self.color
            self.next_update.append(next_cell)
        self.cells = self.next_update
        self.next_update = []
        return True


    def moveLeft(self):
        for cell in self.cells:
            if cell.left is None or cell.left.piled:
                return
        for cell in self.cells:
            cell.color = cell.base_color
        for cell in self.cells:
            next_cell = cell.left
            next_cell.color = self.color
            self.next_update.append(next_cell)
        self.cells = self.next_update
        self.next_update = []

    def moveRight(self):
        for cell in self.cells:
            if cell.right is None or cell.right.piled:
                return
        for cell in self.cells:
            cell.color = cell.base_color
        for cell in self.cells:
            next_cell = cell.right
            next_cell.color = self.color
            self.next_update.append(next_cell)
        self.cells = self.next_update
        self.next_update = []