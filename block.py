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
    def __init__(self, color):
        self.cells = []
        self.next_update = []
        self.color = color

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


class O(Block):

    def __init__(self, anchor):
        super().__init__((155,155,0))
        self.cells.append(anchor)
        self.cells.append(anchor.right)
        self.cells.append(anchor.right.down)
        self.cells.append(anchor.right.down.left)
        for cell in self.cells:
            cell.color = self.color
        
    def rotateLeft(self):
        return

    def rotateRight(self):
        return

class I(Block):

    def __init__(self, anchor):
        super().__init__((0,155,155))
        self.cells.append(anchor)
        self.cells.append(anchor.right)
        self.cells.append(anchor.left)
        self.cells.append(anchor.left.left)
        for cell in self.cells:
            cell.color = self.color
        
    def rotateLeft(self):
        return

    def rotateRight(self):
        return