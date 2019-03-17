import numpy as np

class Pile:
    def __init__(self):
        self.cells = np.array([1])

    def add_block(self, block):
        for cell in block.cells:
            self.cells.append(cell)
            cell.piled = True